max_score = 10  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import (
    normalize_text,
    load_student_code,
    format_error_message,
    exception_message_for_students,
    round_match,
    get_similarity_feedback,
    clear_database,
    pc_get_or_create,
    pc_finalize_and_maybe_fail,
    default_module_to_test
)
import re

# Checks if the expected printed messages actually appear, but doesn't check for specific inputs or correct calculations.
def test_02_printed_messages(current_test_name, input_test_cases):
    try:
        rec = pc_get_or_create(current_test_name, max_score)
        # Ensure test_cases is valid and iterable
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_input_test_case": None}
            exception_message_for_students(ValueError("input_test_cases should be a list of dictionaries. Contact your professor."), input_test_case, current_test_name) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        for input_test_case in input_test_cases:
            case_id = input_test_case["id_input_test_case"]
            phrases_to_replace_number = [
                "results of game",
                "home team",
                "away team",
                "season record",
                "total goals scored",
                "total goals allowed"
            ]
            phrases_to_replace_date = [
                "results of game"
            ]

            inputs = input_test_case["inputs"]

            # because most of the numbers printed are randomly generated or
            # differ depending on what the date is, just replace all the numbers
            # and dates.
            expected_printed_messages = input_test_case["printed_messages"]
            split_expected_printed_messages = []
            for message in expected_printed_messages:
                split_list = message.split("\n")
                if len(split_list) > 1:
                    for split_message in split_list:
                        if split_message:
                            split_expected_printed_messages.append(split_message)
                else:
                    split_expected_printed_messages.append(message)
           
            expected_printed_messages = split_expected_printed_messages
            expected_printed_messages = [re.sub(r'\b(\d{4})-(\d{2})-(\d{2})\b', "<dateplaceholder>", message) for message in expected_printed_messages]
            expected_printed_messages = [normalize_text(printed_message) for printed_message in expected_printed_messages]
            expected_printed_messages = [re.sub('dateplaceholder', "<date>", message) for message in expected_printed_messages]
            expected_printed_messages = [re.sub(r'\d+(?:\.\d+)?', "<number>", message) for message in expected_printed_messages]

            invalid_printed_messages = input_test_case["invalid_printed_messages"]

            # Load in the student's code and capture output
            manager_payload = load_student_code(current_test_name, inputs, input_test_case, default_module_to_test)
            
            if not manager_payload:
                continue # if there was an error in running student code, it's already been logged. Just skip to the next test case.

            captured_output = manager_payload.get('captured_output')
            captured_lines = captured_output.splitlines()
            # Normalize the captured input prompts to remove spaces, punctuation, and symbols
            normalized_captured_print_statements_list = [re.sub(r'\b(\d{4})-(\d{2})-(\d{2})\b', "<dateplaceholder>", message) for message in captured_lines]
            normalized_captured_print_statements_list = [normalize_text(captured_print) for captured_print in normalized_captured_print_statements_list]
            normalized_captured_print_statements_list = [re.sub('dateplaceholder', "<date>", message) for message in normalized_captured_print_statements_list]
            normalized_captured_print_statements_list = [re.sub(r'\d+(?:\.\d+)?', "<number>", message) for message in normalized_captured_print_statements_list]
            normalized_captured_print_statements_str = ' '.join(normalized_captured_print_statements_list)
            normalized_captured_print_statements_list = list(dict.fromkeys(normalized_captured_print_statements_list)) # get rid of duplicates
            # create string of all print statements to search for for matches.
            
            # create a version for error messages if needed
            error_message_print_statements = [f'{index}: "{output}"' for index, output in enumerate(normalized_captured_print_statements_list, start=1)]
            # create string version for error messages if needed
            error_message_print_statements_str = '\n'.join(error_message_print_statements)
            
            case_failed_messages = []  # collect case's failure messages (exactly as before)


            # Check that each required phrase (regex pattern) is found in the normalized captured output
            for expected_phrase in expected_printed_messages:

                # Skip over phrases that should only sometimes print
                phrases_to_skip = ["qualified for the ncaa soccer tournament", "you had a good season", "your team needs to practice"]
                skip_iteration = False
                for skip_phrase in phrases_to_skip:
                    if skip_phrase in expected_phrase:
                        skip_iteration = True
                        break
                if skip_iteration:
                    continue

                # Check if the pattern exists in the normalized captured print statements
                match = re.search(expected_phrase, normalized_captured_print_statements_str)

                # if there isn't a match, prepare the strings for the failure message to make it less confusing.
                if not match:
                    similarity_message = get_similarity_feedback(expected_phrase, normalized_captured_print_statements_list)

                    # Build the EXACT same formatted message (but don't assert now)
                    formatted = format_error_message(
                        custom_message=("The expected printed message (ignoring punctuation / capitalization):\n\n"
                                        f"```\n\"{expected_phrase}\"\n```\n"
                                        f"wasn't printed in your code.\n\n"
                                        f"### How to fix it:\n"
                                        f"Likely, the error is from one of 3 causes:\n"
                                        f"1. You made a spelling error.\n"
                                        f"2. You forgot to include the expected printed message.\n"
                                        f"3. The logic in your code makes the correct message not appear or makes it include incorrect content.\n\n"
                                        f"#### Possible spelling mistakes:\n"
                                        f"To help you rule out possible cause #1, below are printed messages that appear in your code that are really close the the printed message you're missing.\n"
                                        f"```\n{similarity_message}\n```\n"
                                        f"#### All your printed messages:\n"
                                        f"Below are all the unique printed messages from when the test ran your code (ignoring punctuation and capitalization). Make sure you are including the needed message and spelling it correctly!:\n\n"
                                        f"```\n{error_message_print_statements_str}\n```\n"),
                        current_test_name=current_test_name,
                        input_test_case=input_test_case,
                        display_inputs=True,
                    )
                    case_failed_messages.append(formatted)

            # Ensure none of the invalid phrases are found in the normalized captured output
            for invalid_phrase in invalid_printed_messages:
                invalid_phrase = normalize_text(invalid_phrase)

                # Skip over phrases that should only sometimes print
                phrases_to_skip = ["qualified for the ncaa soccer tournament", "you had a good season", "your team needs to practice", "game info menu", "team info menu"]
                skip_iteration = False
                for skip_phrase in phrases_to_skip:
                    if skip_phrase in invalid_phrase:
                        skip_iteration = True
                        break
                if skip_iteration:
                    continue

                regex_pattern = invalid_phrase.replace("<wildcard>", r".+?")
                match = re.search(regex_pattern, normalized_captured_print_statements_str)

                if match:
                    formatted = format_error_message(
                        custom_message=("You used an invalid printed message (ignoring punctuation / capitalization):\n\n"
                                        f"```\n\"{invalid_phrase}\"\n```\n"
                                        f"### How to fix it:\n"
                                        f"Most likely:\n"
                                        f"1. You are printing something that should be inside an if statement or while loop, but isn't.\n"
                                        f"2. You are printing something that IS in an if statement or while loop, but you wrote the logic incorrectly so it appears when it shouldn't.\n"
                                        f"#### All your printed output:\n"
                                        f"Below are all the unique printed messages from when the test ran your code (ignoring punctuation and capitalization). Make sure you aren't including the invalid message!:\n\n"
                                        f"```\n{error_message_print_statements_str}\n```\n"),
                        current_test_name=current_test_name,
                        input_test_case=input_test_case,
                        display_inputs=True
                    )
                    case_failed_messages.append(formatted)

            # Record the case result for partial credit
            if case_failed_messages:
                # Join multiple messages (if both a required and invalid check failed)
                full_msg = "\n\n".join(case_failed_messages)
                rec.fail_case(case_id, reason="printed message mismatch", custom_message=full_msg)
            else:
                rec.pass_case(case_id)
                
    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, input_test_case, current_test_name)

    finally:
        # After all cases, emit a one-line summary or a short failure directing to the MD file
        pc_finalize_and_maybe_fail(rec)

  