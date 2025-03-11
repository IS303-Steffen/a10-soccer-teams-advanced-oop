# Game Class Tests

## Game Class Test 1

### Initial Arguments
````
game_number: 1 - int
home_team: {'class_name': 'SoccerTeam', 'init_args': [1, 'UVU']} - dict
away_team: {'class_name': 'SponsoredTeam', 'init_args': [2, 'BYU', 'Cosmo']} - dict
````

### Expected Initial Values
````
game_number: 1 - int
game_date: 2025-03-11 - date
home_team: {'team_number': 1, 'team_name': 'UVU', '_SoccerTeam__wins': 0, '_SoccerTeam__losses': 0, 'goals_scored': 0, 'goals_allowed': 0} - dict
away_team: {'team_number': 2, 'team_name': 'BYU', 'sponsor_name': 'Cosmo', '_SoccerTeam__wins': 0, '_SoccerTeam__losses': 0, 'goals_scored': 0, 'goals_allowed': 0} - dict
home_team_score: 0 - int
away_team_score: 0 - int
````

### Expected Method Names
````
get_game_status
play_game
````

