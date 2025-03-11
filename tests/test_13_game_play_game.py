max_score = 13  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import load_student_code, format_error_message, exception_message_for_students, normalize_text, prettify_dictionary
#from test_cases_classes_final import class_test_cases
from collections.abc import Iterable
import pytest

def test_13_game_play_game(current_test_name, input_test_cases, class_test_cases):
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_test_case": None}
            exception_message_for_students(ValueError("test_cases should be a list of dictionaries. Contact your professor."), input_test_case=input_test_case) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        # Use the appropriate test case
        input_test_case = input_test_cases[0]
        inputs = input_test_case["inputs"]

        # Name of the class being tested:
        class_name = "Game"
        method_to_test = 'play_game'
        class_test_cases_payload = {'class_name': class_name}
        class_test_cases_payload['class_test_cases'] = class_test_cases.get(class_name)
        class_test_cases_payload['test_type'] = 'method_test'
        class_test_cases_payload['method_to_test'] = method_to_test

        # Load the student's code and test classes
        manager_payload = load_student_code(current_test_name, inputs, input_test_case, class_tests=class_test_cases_payload)

        # first check if there was an error trying to run the code
        if manager_payload.get('class_results').get('CLASS ERROR') is not None:
            custom_message = f"{manager_payload.get('class_results').get('CLASS ERROR').get('message')}\n\n"
            formatted_message = format_error_message(
                                    custom_message=custom_message, 
                                    input_test_case=input_test_case,
                                    current_test_name=current_test_name)
            pytest.fail(formatted_message)

        elif manager_payload.get('class_results').get('FUNCTION ERROR') is not None:
            exception_message_for_students(
                exception_data=manager_payload.get('class_results').get('FUNCTION ERROR').get("FUNCTION ERROR"),
                input_test_case=input_test_case,
                current_test_name=current_test_name,
                )

        class_results_list = manager_payload.get('class_results').get('class_test_cases')

        # loop through each class test case
        for class_result in class_results_list:
            
            # get results of the methods we are looking at:
            method_results_list = [method_result for method_result in class_result.get('method_test_cases') if method_result.get('function_name') == method_to_test]
            
            if not method_results_list:
                exception_message = exception_message_for_students(ValueError("No method test cases were found. Contact your professor."), input_test_case, current_test_name)
                pytest.fail(exception_message)

            for method_result in method_results_list:
                # first check if there were any function errors when running the method:
                if method_result.get('FUNCTION ERROR') is not None:
                    exception_message = exception_message_for_students(
                                            exception_data=method_result.get('FUNCTION ERROR'), 
                                            input_test_case=input_test_case,
                                            current_test_name=current_test_name,
                                            )
                    pytest.fail(exception_message)
                    
                # I want to go through each variable that needsto be updated and check if it was updated for each home and away team.
                initial_game = method_result.get('initial_obj_state')[0].get('instance_variables')
                final_home = method_result.get('final_obj_state')[0].get('instance_variables').get('home_team').get('instance_variables')      
                final_away = method_result.get('final_obj_state')[0].get('instance_variables').get('away_team').get('instance_variables')
                final_game = method_result.get('final_obj_state')[0].get('instance_variables')

                updated_values = {
                    "updated_game_score": False,
                    "updated_wins": False,
                    "updated_losses": False,
                    "updated_goals_scored": False,
                    "updated_goals_allowed": False
                }

                if final_game.get('home_team_score') > 0 or final_game.get('away_team_score') > 0:
                    updated_values['updated_game_score'] = True 

                if final_home.get('_SoccerTeam__wins') == 1 or final_away.get('_SoccerTeam__wins') == 1:
                    updated_values['updated_wins'] = True

                if final_home.get('_SoccerTeam__losses') == 1 or final_away.get('_SoccerTeam__losses') == 1:
                    updated_values['updated_losses'] = True

                # because of no tie scores, they can't both be zero
                if final_home.get('goals_scored') > 0 or final_away.get('goals_scored') > 0:
                    updated_values['updated_goals_scored'] = True

                if final_home.get('goals_allowed') > 0 or final_away.get('goals_allowed')  > 0:
                    updated_values['updated_goals_allowed'] = True

                updated_values_str = prettify_dictionary(updated_values)
                inital_game_str = prettify_dictionary(initial_game)
                final_game_str = prettify_dictionary(final_game)

                assert False not in list(updated_values.values()), format_error_message(
                    custom_message=(f"The method \"{method_to_test}\" is meant to update the following:\n\n"
                                    f"VALUES THAT {method_to_test.upper()} SHOULD UPDATE:\n"
                                    f"---------------------------------------------------\n"
                                    f"{updated_values_str}\n\n"
                                    f"But any \"False\" values above mean you did not properly update that value for your Game (or the team objects inside the game)."
                                    f"Below are the starting values in the Game class, followed by the values after {method_to_test} "
                                    f"is run. Make sure the after values are all being updated as they should to be according to the instructions."
                                    f"BEFORE RUNNING {method_to_test.upper()}:\n"
                                    f"{'-'*len(f'BEFORE RUNNING {method_to_test.upper()}:')}\n"
                                    f"{inital_game_str}\n\n"
                                    f"AFTER RUNNING {method_to_test.upper()}:\n"
                                    f"{'-'*len(f'AFTER RUNNING {method_to_test.upper()}:')}\n"
                                    f"{final_game_str}\n\n"
                                    f"Make sure all the necessary variables are being updated, either in the Game's score, or the nested "
                                    f"soccer team objects."),
                    current_test_name=current_test_name,
                    input_test_case=input_test_case,
                    )
    
    except AssertionError:
        raise
    except Exception as e:
        exception_message_for_students(e, input_test_case, current_test_name)

