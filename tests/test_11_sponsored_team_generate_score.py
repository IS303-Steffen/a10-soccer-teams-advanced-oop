max_score = 5  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import (
    normalize_text,
    load_student_code,
    format_error_message,
    exception_message_for_students,
    prettify_dictionary,
    pc_get_or_create,
    pc_finalize_and_maybe_fail,
    unmangle_keys,
    unmangle_name,
    default_module_to_test
)

def test_11_sponsored_team_generate_score(current_test_name, input_test_cases, class_test_cases):
    try:
        rec = pc_get_or_create(current_test_name, max_score)
        # Ensure test_cases is valid and iterable
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_test_case": None}
            exception_message_for_students(ValueError("test_cases should be a list of dictionaries. Contact your professor."), input_test_case=input_test_case) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        # Use the appropriate test case
        input_test_case = input_test_cases[0]
        inputs = input_test_case["inputs"]

        # Name of the class being tested:
        class_name = "SponsoredTeam"
        method_to_test = 'generate_score'
        class_test_cases_payload = {'class_name': class_name}
        class_test_cases_payload['class_test_cases'] = class_test_cases.get(class_name)
        class_test_cases_payload['test_type'] = 'method_test'
        class_test_cases_payload['method_to_test'] = method_to_test

        # Load the student's code and test classes
        manager_payload = load_student_code(current_test_name, inputs, input_test_case, class_tests=class_test_cases_payload)

        if not manager_payload:
            return # if there was an error in running student code, it's already been logged. Just skip to the next test case.

        # first check if there was an error trying to run the code
        if manager_payload.get('class_results').get('CLASS ERROR') is not None:
            custom_message = f"{manager_payload.get('class_results').get('CLASS ERROR').get('message')}\n\n"
            formatted_message = format_error_message(
                                    custom_message=custom_message, 
                                    input_test_case=input_test_case,
                                    current_test_name=current_test_name)
            rec.fail_case(
                case_id=f"class:{class_name}:setup",
                custom_message=formatted_message,
                case_type="class",
                label=f"{class_name} (setup)"
            )
            return

        elif manager_payload.get('class_results').get('FUNCTION ERROR') is not None:
            exception_message_for_students(
                exception_data=manager_payload.get('class_results').get('FUNCTION ERROR').get("FUNCTION ERROR"),
                input_test_case=input_test_case,
                current_test_name=current_test_name,
                )
            return # the failure is already recorded by the function above, so just end this test.

        class_results_list = manager_payload.get('class_results').get('class_test_cases')

        # loop through each class test case
        for class_result in class_results_list:
            
            # get results of the methods we are looking at:
            method_results_list = [method_result for method_result in class_result.get('method_test_cases') if method_result.get('function_name') == method_to_test]
            
            if not method_results_list:
                exception_message_for_students(ValueError("No method test cases were found. Contact your professor."), input_test_case, current_test_name)
                return
                
            for index, method_result in enumerate(method_results_list, start=1):
                # first check if there were any function errors when running the method:
                if method_result.get('FUNCTION ERROR') is not None:
                    exception_message_for_students(
                                            exception_data=method_result.get('FUNCTION ERROR'), 
                                            input_test_case=input_test_case,
                                            current_test_name=current_test_name,
                                            )
                    return

                expected_return_value = normalize_text(method_result.get('expected_return_value'))
                required_expected_values = {x:"Not found" for x in range(expected_return_value[0], expected_return_value[1]+1)}

                actual_returned_values_list = method_result.get('actual_return_value')
                if isinstance(actual_returned_values_list, list):
                    actual_returned_values_list = list(dict.fromkeys(sorted(actual_returned_values_list)))

                for number in required_expected_values:
                    if number in actual_returned_values_list:
                        required_expected_values[number] = 'Found'
                        actual_returned_values_list.remove(number)
                
                numbers_dict_str = prettify_dictionary(required_expected_values)
                extra_numbers_str = str(actual_returned_values_list) if len(actual_returned_values_list) > 0 else "No invalid values found"
                
                valid_numbers_found = "Not found" not in list(required_expected_values.values())
                no_extra_numbers_found = len(actual_returned_values_list) == 0

                if not valid_numbers_found or not no_extra_numbers_found:
                    formatted = format_error_message(
                    custom_message=(f"The method {method_to_test} should only be generating values from {expected_return_value[0]} to {expected_return_value[1]} (inclusive)\n\n"
                                    f"### Necessary numbers:\n"
                                    f"```\n{numbers_dict_str}\n```\n"
                                    f"### Invalid numbers:\n"
                                    f"These are invalid numbers that your code is generating:\n"
                                    f"```\n{extra_numbers_str}\n```\n"
                                    f"If you aren't generating valid numbers or are generating invalid numbers, make sure the range of numbers in your random number generating logic follows "
                                    f"the logic given in the instructions."),
                    current_test_name=current_test_name,
                    input_test_case=input_test_case,
                    )
                    rec.fail_case(case_id=f"method:{class_name}-{method_to_test}:{index}",  custom_message=formatted, case_type="method")
                else:
                    rec.pass_case(case_id=f"method:{class_name}-{method_to_test}:{index}", case_type="method")
                
    except AssertionError:
        raise
    except Exception as e:
        exception_message_for_students(e, input_test_case, current_test_name)
    finally:
        pc_finalize_and_maybe_fail(rec)