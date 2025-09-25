max_score = 13  # This value is pulled by yml_generator.py to assign a score to this test.
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

# Treat a serialized instance_variables dict from a team object.
# Unmangles keys and returns a dict like {"__wins": 1, "__losses": 0, "goals_scored": 3, ...}
def _logical_team_vars(team_instance_vars: dict) -> dict:
    # 1) unmangle any _Class__tail keys to logical names like __wins
    logical = unmangle_keys(team_instance_vars or {})
    # 2) normalize: some students might use single underscore or public names for goals
    #    (we don't lowercase keys here—we preserve "__wins" naming)
    return logical

# True if ANY of the keys that should be positive were updated.
def _is_positive(v):
    try:
        return (v or 0) > 0
    except Exception:
        return False
    
# ---- Robust key lookup helpers ----
def _variants_for(base: str):
    """
    Given a logical snake_case name (e.g., 'home_team_score'),
    return acceptable variants: snake, camel, Pascal.
    """
    parts = base.split('_')
    pascal = ''.join(p.capitalize() for p in parts)
    camel = parts[0] + ''.join(p.capitalize() for p in parts[1:])
    snake = base
    return [snake, camel, pascal]

def _find_key(d: dict, logical_name: str):
    """
    Try to find a key in dict 'd' allowing snake/camel/Pascal variants
    AND a final fallback that compares keys with underscores removed + casefold.
    Returns (found_bool, actual_key or None).
    """
    if not isinstance(d, dict):
        return False, None
    # 1) Direct attempts with explicit variants
    for k in _variants_for(logical_name):
        if k in d:
            return True, k
    # 2) Fallback: normalize all keys by stripping underscores and casefolding
    target = logical_name.replace('_', '').casefold()
    for k in d.keys():
        if isinstance(k, str) and k.replace('_', '').casefold() == target:
            return True, k
    return False, None

def _pick(d: dict, logical_name: str):
    """
    Convenience: return the value and actual key for 'logical_name' from dict 'd'.
    If not found, returns (None, None).
    """
    ok, key = _find_key(d, logical_name)
    if not ok:
        return None, None
    return d.get(key), key

def _canonicalize_team_vars(d: dict) -> dict:
    """
    Given a team's instance_variables dict (already unmangled), return a dict
    with canonical keys so comparisons are style-agnostic:
      - '__Wins' / '__WINS' -> '__wins'
      - 'wins' / '_wins'    -> '__wins'
      - 'losses' / '_losses' -> '__losses'
      - 'goalsScored' / 'GoalsScored' -> 'goals_scored'
      - 'goalsAllowed' / 'GoalsAllowed' -> 'goals_allowed'
    """
    if not isinstance(d, dict):
        return d

    out = {}
    for k, v in d.items():
        nk = k
        if isinstance(nk, str):
            # Private: normalize tail to lowercase
            if nk.startswith("__") and not nk.startswith("___"):
                nk = "__" + nk[2:].lower()
            else:
                # Compact form for public/protected names
                compact = nk.replace("_", "").casefold()

                # wins / losses -> canonical private names
                if compact == "wins":
                    nk = "__wins"
                elif compact == "losses":
                    nk = "__losses"
                # goals_* to snake case canonical
                elif compact == "goalsscored":
                    nk = "goals_scored"
                elif compact == "goalsallowed":
                    nk = "goals_allowed"
                # otherwise leave as-is

        out[nk] = v
    return out



def test_13_game_play_game(current_test_name, input_test_cases, class_test_cases):
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
        class_name = "Game"
        method_to_test = 'play_game'
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
            return

        class_results_list = manager_payload.get('class_results').get('class_test_cases')

        # loop through each class test case
        for class_result in class_results_list:
            
            # get results of the methods we are looking at:
            method_results_list = [method_result for method_result in class_result.get('method_test_cases') if method_result.get('function_name') == method_to_test]
            
            if not method_results_list:
                exception_message_for_students(ValueError("No method test cases were found. Contact your professor."), input_test_case, current_test_name)
                return
            
            case_failed_messages = []
            for index, method_result in enumerate(method_results_list, start=1):
                # first check if there were any function errors when running the method:
                if method_result.get('FUNCTION ERROR') is not None:
                    exception_message_for_students(
                                            exception_data=method_result.get('FUNCTION ERROR'), 
                                            input_test_case=input_test_case,
                                            current_test_name=current_test_name,
                                            )
                    return
                    
                # Pull initial/final game state
                initial_game = method_result.get('initial_obj_state')[0].get('instance_variables')
                final_state   = method_result.get('final_obj_state')[0].get('instance_variables')

                # ---- Robustly unwrap nested teams (home/away) regardless of naming style ----
                home_team_dict, home_key = _pick(final_state, 'home_team')
                away_team_dict, away_key = _pick(final_state, 'away_team')

                missing_keys = []
                if home_team_dict is None or not isinstance(home_team_dict, dict) or 'instance_variables' not in home_team_dict:
                    missing_keys.append("home team object valid names: " + ', '.join(_variants_for('home_team')) + ")")
                if away_team_dict is None or not isinstance(away_team_dict, dict) or 'instance_variables' not in away_team_dict:
                    missing_keys.append("home team object valid names: " + ', '.join(_variants_for('away_team')) + ")")

                if missing_keys:
                    missing_keys_msg = '\n'.join(missing_keys)
                    msg = ("The Game object did not include the expected nested team object(s):\n"
                           f"```\n{missing_keys_msg}\n```\n"
                           f"Make sure your Game has both a home and away team stored as objects. You can "
                           f" name them in snake_case, camelCase, or PascalCase.")
                    formatted = format_error_message(custom_message=msg, current_test_name=current_test_name, input_test_case=input_test_case)
                    case_failed_messages.append(formatted)
                    # Skip further checks for this method_result
                    continue

                final_home_raw = home_team_dict.get('instance_variables') or {}
                final_away_raw = away_team_dict.get('instance_variables') or {}

                # Unmangle ALL keys inside the team dicts so __wins/__losses are logical, regardless of class name/case
                final_home = _canonicalize_team_vars(_logical_team_vars(final_home_raw))
                final_away = _canonicalize_team_vars(_logical_team_vars(final_away_raw))


                # ---- Robustly fetch game scores regardless of naming style ----
                home_score, home_score_key = _pick(final_state, 'home_team_score')
                away_score, away_score_key = _pick(final_state, 'away_team_score')

                # If your students might rename these too, fail gracefully if missing
                if home_score is None or away_score is None:
                    msg = ("The Game object did not include expected score fields:\n"
                        f"- home_team_score (also accepts: {', '.join(_variants_for('home_team_score'))})\n"
                        f"- away_team_score (also accepts: {', '.join(_variants_for('away_team_score'))})")
                    formatted = format_error_message(custom_message=msg, current_test_name=current_test_name, input_test_case=input_test_case)
                    case_failed_messages.append(formatted)
                    continue

                # Also unmangle the top-level game dict for clean printing later
                initial_game_unmangled = unmangle_keys(initial_game)
                final_game = unmangle_keys(final_state)

                # Also canonicalize the nested team dicts inside the print views (if present)
                for team_slot in ("home_team", "homeTeam", "HomeTeam", "away_team", "awayTeam", "AwayTeam"):
                    slot = final_game.get(team_slot)
                    if isinstance(slot, dict) and "instance_variables" in slot:
                        slot["instance_variables"] = _canonicalize_team_vars(
                            _logical_team_vars(slot["instance_variables"])
                        )
                    slot0 = initial_game_unmangled.get(team_slot)
                    if isinstance(slot0, dict) and "instance_variables" in slot0:
                        slot0["instance_variables"] = _canonicalize_team_vars(
                            _logical_team_vars(slot0["instance_variables"])
                        )

                updated_values = {
                    "updated_game_score": False,
                    "updated_wins": False,
                    "updated_losses": False,
                    "updated_goals_scored": False,
                    "updated_goals_allowed": False
                }

                # Game score updated?
                if _is_positive(home_score) or _is_positive(away_score):
                    updated_values['updated_game_score'] = True


                # Wins/Losses updated on either team (check logical names, not class-mangled)
                # One of the teams should have wins == 1 and the other losses == 1 after a game.
                if (final_home.get('__wins') == 1) or (final_away.get('__wins') == 1):
                    updated_values['updated_wins'] = True

                if (final_home.get('__losses') == 1) or (final_away.get('__losses') == 1):
                    updated_values['updated_losses'] = True

                # Goals updated on either team
                if _is_positive(final_home.get('goals_scored')) or _is_positive(final_away.get('goals_scored')):
                    updated_values['updated_goals_scored'] = True

                if _is_positive(final_home.get('goals_allowed')) or _is_positive(final_away.get('goals_allowed')):
                    updated_values['updated_goals_allowed'] = True


                updated_values_str = prettify_dictionary(updated_values)
                inital_game_str = prettify_dictionary(initial_game_unmangled)
                final_game_str  = prettify_dictionary(final_game)


                if False in list(updated_values.values()):
                    formatted = format_error_message(
                        custom_message=(f"The method \"{method_to_test}\" is meant to update the following:\n\n"
                                        f"### Values that {method_to_test} should update:\n"
                                        f"```\n{updated_values_str}\n```\n"
                                        f"But any \"False\" values above mean you did not properly update that value for your Game (or the team objects inside the game)."
                                        f"Below are the starting values in the Game class, followed by the values after {method_to_test} "
                                        f"is run. Make sure the after values are all being updated as they should to be according to the instructions.\n"
                                        f"### Your values before running {method_to_test}:\n"
                                        f"```\n{inital_game_str}\n```\n"
                                        f"### Your values after running {method_to_test}:\n"
                                        f"```\n{final_game_str}\n```\n"
                                        f"Make sure all the necessary variables are being updated, either in the Game's score, or the nested "
                                        f"soccer team objects."),
                        current_test_name=current_test_name,
                        input_test_case=input_test_case,
                        )
                    case_failed_messages.append(formatted)
            
            # Record the case result for partial credit
            if case_failed_messages:
                # Join multiple messages (if both a required and invalid check failed)
                full_msg = "\n\n".join(case_failed_messages)
                rec.fail_case(case_id=f"method:{class_name}-{method_to_test}:{index}",  custom_message=full_msg, case_type="method")
            else:
                rec.pass_case(case_id=f"method:{class_name}-{method_to_test}:{index}", case_type="method")
    
    except AssertionError:
        raise
    except Exception as e:
        exception_message_for_students(e, input_test_case, current_test_name)
    finally:
        pc_finalize_and_maybe_fail(rec)