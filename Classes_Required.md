
## Classes Required:

### IMPORTANT:
Please use the same capitalization case as what is shown in these instructions for all the class names and variables, otherwise the automated tests might break. For example, please call your class `SoccerTeam`, NOT `soccerTeam` or `soccer_team`, etc. I'll try and improve the automated tests in a future semester to account for alternate spellings. Sorry for any annoyance that causes you.

#### `SoccerTeam`
- Instance Variables:
    - `team_number`: (int) the number (1, 2, 3, etc.) of the team.
    - `team_name`: (str) name of the team.
    - `wins`: (int) stores the number of wins. Defaults to 0. It MUST be a private variable (meaning it shouldn't just be called "wins").
    - `losses`: (int) stores the number of losses. Defaults to 0. It MUST be a private variable (meaning it shouldn't just be called "losses").
    - `goals_scored`: (int) the total number goals they have scored across all games. Defaults to 0.
    - `goals_allowed`: (int) the total number of goals other teams scored on them across all games. Defaults to 0.
- Methods
    - `__init__`
        - The constructor. It must accept parameters that go in to `team_number` and `team_name`.
    - `record_win`
        - adds 1 to the `wins` private variable.
    - `record_loss`
        - adds 1 to the `losses` private variable.
    - `get_record_percentage`
        - returns the season record as a percentage (wins / total games played) rounded to the 2nd decimal. Needs to handle any potential zero division errors.
    - `get_team_info`
        - returns info on the team and their performance.
    - `generate_score`
        - returns a randomly generated score between 0 and 3.
    - `get_season_message`
        - returns a message based on the team’s win rate.
#### `SponsoredTeam` (inherits from `SoccerTeam`)
- Instance Variables:
    - All of the instance variables from SoccerTeam through the use of super().
    - `sponsor_name`: (str) the name of the sponsor for the team.
- Methods
    - `__init__`
        - The constructor. Should call the SoccerTeam constructor.  It must accept parameters that go in to `team_number`, `team_name`, and `sponsor_name`.
    - `generate_score`
        - Overrides the SoccerTeam version. Returns a randomly generated score between 1 and 3.
    - `get_season_message`
        - Overrides the SoccerTeam version. Returns a message based on the team’s win rate, and also mentions how their sponsor feels about their performance.
#### `Game`
- Instance variables:
    - `game_number`: (int) the number of the game (1, 2, 3, etc.).
    - `game_date`: (date) the date the game was played.
    - `home_team`: (Soccer/Sponsored Team) team object of the home team.
    - `away_team`: (Soccer/Sponsored Team) team object of the away team.
    - `home_team_score`: (int) how many points the home team scored during the game. Defaults to 0.
    - `away_team_score`: (int) how many points the away team scored during the game. Defaults to 0.
- Methods:
    - `__init__`
        - The constructor. It must accept parameters that go into `game_number`, `home_team`, and `away_team`.
    - `get_game_status`
        - returns a string with the date of the game and how many points the home and away teams scored and the team names.
    - `play_game`
        - generates scores for the home and away team objects, and updates the `Game`'s scores, and the teams' `goals_scored`, `goals_allowed`, `wins`, `losses`, and calls the `get_game_status`.
