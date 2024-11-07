from datetime import date, timedelta

# ======================
# METHOD TEST CASE CLASS
# ======================

class MethodTestCase:
    def __init__(self, function_name, args, expected_return_value, expected_object_update=None, num_calls=1):
        self.function_name = function_name
        self.args = args
        self.expected_return_value = expected_return_value
        self.expected_object_update = expected_object_update
        self.num_calls = num_calls

    def to_dict(self):
        return {
            "function_name": self.function_name,
            "args": self.args,
            "expected_return_value": self.expected_return_value,
            "expected_object_update": self.expected_object_update,
            "num_calls": self.num_calls
        }
    
# ======================
# CLASS TEST CASE CLASS
# ======================

class ClassTestCase:
    def __init__(self, class_name, init_args, init_expected_values, expected_function_names, method_test_cases):
        self.class_name = class_name
        self.init_args = init_args
        self.init_expected_values = init_expected_values
        self.expected_function_names = expected_function_names
        self.method_test_cases = [m.to_dict() for m in method_test_cases]

    def to_dict(self):
        return {
            "class_name": self.class_name,
            "init_args": self.init_args,
            "init_expected_values": self.init_expected_values,
            "expected_function_names": self.expected_function_names,
            "method_test_cases": self.method_test_cases
        }

    @classmethod
    def from_dict(cls, data):
        method_test_cases = [MethodTestCase(**m) for m in data["method_test_cases"]]
        return cls(
            class_name=data["class_name"],
            init_args=data["init_args"],
            init_expected_values=data["init_expected_values"],
            expected_function_names=data["expected_function_names"],
            method_test_cases=method_test_cases
        )
    
# ==============================
# CREATE TEST CASE OBJECTS BELOW
# ==============================
'''
MethodTestCase objects should be created first, then placed inside of ClassTestCase
objects in their method_test_cases attribute
'''

# ========================
# METHOD TEST CASE OBJECTS
# ========================

# Creating MethodTestCase objects for the 'SoccerTeam' class test cases
soccer_team_get_info = MethodTestCase(
    function_name='record_win',
    args=[],
    expected_return_value=None,
    expected_object_update=None
)



# =======================
# CLASS TEST CASE OBJECTS
# =======================

UVU_soccer_team = ClassTestCase(
    class_name='SoccerTeam',
    init_args={
        'team_number': 1,
        'team_name': 'UVU',
    },
    init_expected_values={
        'team_number': 1,
        'team_name': 'UVU',
        '_SoccerTeam__wins': 0,
        '_SoccerTeam__losses': 0,
        'goals_scored': 0,
        'goals_allowed': 0
    },
    expected_function_names=['record_win', 'record_loss', 'get_record_percentage', 'get_team_info', 'generate_score', 'get_season_message'],
    method_test_cases=[]
)

BYU_sponsored_team = ClassTestCase(
    class_name='SponsoredTeam',
    init_args={
        'team_number': 2,
        'team_name': 'BYU',
        'sponsor_name': 'Cosmo'
    },
    init_expected_values={
        'team_number': 2,
        'team_name': 'BYU',
        'sponsor_name': 'Cosmo',
        '_SoccerTeam__wins': 0,
        '_SoccerTeam__losses': 0,
        'goals_scored': 0,
        'goals_allowed': 0
    },
    expected_function_names=['record_win', 'record_loss', 'get_record_percentage', 'get_team_info', 'generate_score', 'get_season_message'],
    method_test_cases=[]
)

game_1 = ClassTestCase(
    class_name='Game',
    init_args={
        'game_number': 1,
        'home_team': {'class_name': 'SoccerTeam', 'init_args': [1, 'UVU']},
        'away_team': {'class_name': 'SponsoredTeam', 'init_args': [2, 'BYU', 'Cosmo']}
    },
    init_expected_values={
        'game_number': 1,
        'game_date': date.today() + timedelta(days=1),
        'home_team': {'team_number': 1, 'team_name': 'UVU', '_SoccerTeam__wins': 0, '_SoccerTeam__losses': 0, 'goals_scored': 0, 'goals_allowed': 0},
        'away_team': {'team_number': 2, 'team_name': 'BYU', 'sponsor_name': 'Cosmo', '_SoccerTeam__wins': 0, '_SoccerTeam__losses': 0, 'goals_scored': 0, 'goals_allowed': 0},
        'home_team_score': 0,
        'away_team_score': 0
    },
    expected_function_names=['simulate', 'get_winner', 'get_loser', 'update_records'],
    method_test_cases=[]
)

# Update the list of test cases
test_cases_classes_list = [UVU_soccer_team, BYU_sponsored_team, game_1]

test_cases_classes_list = [class_test_case.to_dict() for class_test_case in test_cases_classes_list]
unique_class_names = {class_name.get('class_name') for class_name in test_cases_classes_list}

test_cases_classes_dict = {}
for class_name in unique_class_names:
    subset_test_cases_classes = [test_case_class for test_case_class in test_cases_classes_list if test_case_class.get('class_name') == class_name]
    test_cases_classes_dict[class_name] = subset_test_cases_classes
