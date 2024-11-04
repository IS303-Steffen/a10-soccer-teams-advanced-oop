#### Assignment 9
# Soccer Teams Inheritance

This assignment uses some of the logic from the previous Soccer Teams assignment, but adds in these concepts:
- OOP
    - association
    - inheritance
    - private variables
- error handling.

Now you'll create `Game` objects that store a home team and away team object. Teams can be regular `SoccerTeam` objects or `SponsoredTeam` objects with modified behavior. Any 2 teams can "play" as many games as they want, all while storing data about the games and teams in their objects. After all games have been played the user can view all the data from any team or any game.

Coding all this requires more work setting everything up compared to the previous Soccer Teams assignment, but hopefully this assignment shows how storing data inside objects allows for more complex interactions (imagine storing all this data in individual variables or other data structures)

## Libraries Required:
- `random`
- `datetime`
    - add `from datetime import date, timedelta` near the top of your code.

<h3 id="classesrequired">Classes Required:</h3>

#### `SoccerTeam`
- Instance Variables:
    - `team_number`: (int) the number (1, 2, 3, etc.) of the team.
    - `team_name`: (str) name of the team.
    - `wins`: (int) stores the number of wins. Defaults to 0. It MUST be a private variable.
    - `losses`: (int) stores the number of losses. Defaults to 0. It MUST be a private variable.
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

## Logical Flow:
For this assignment, you will need to handle improper inputs to receive full credit. You can do it using exception handling or a defensive coding style, whatever you prefer. If you prefer a more defensive style of coding, you might find the `isdigit()` string method useful to tell whether an input is an integer or not. <a href="https://chatgpt.com/share/6725552e-5bdc-8009-8b23-ab682e98f965" target="_blank">Click here for an example of how it is used.</a>

### 1. Ask for the number of soccer teams to create
Ask the user:
- `Enter the number of soccer teams you want to enter (at least 2): `

Make sure your code can handle:
1. extra white space before or after an input
    - e.g. " 2 " should work the same as "2"
2. input that isn't an integer
    - e.g. if they enter "asdf" it should print:
        `Invalid integer! Try again.`
3. input that is under 2:
    - e.g. if they enter 1, 0, or a negative number, it should print:
        `You must enter an integer of 2 or above. Try again.`
- After 2. or 3. ask the user to enter the number of soccer teams again until a valid input is provided.

### 2. Create the `SoccerTeam` or `SponsoredTeam` objects
For the number of teams that the user enters in the previous section, do the following:
- Ask the user:
    - `Enter a name for team <team number>: `
    - So, if it is the first team you are making it would be:
         `Enter a name for team 1: `, etc.
- Then, ask the user:
    - `Enter Y if team <team_number> is sponsored, otherwise enter N (or anything else): `
    - Make sure this wil work even if the user enters a lower case "y" or enters it with extra spaces. So "y" " y ", " Y", and "Y" should all work.
- If the user entered "Y" (or its accepted variations) then ask:
    - `Enter the name of your sponsor: `
    - Create a `SponsoredTeam` object using a team number (should be 1 for the 1st team created, 2 for the 2nd, etc.), as well as the team name and sponsor name that you gathered. The `SponsoredTeam` class should inherit from their parent class of `SoccerTeam`. See the <a href="#classesrequired">Classes Required</a> section of this document for the necessary instance variables for `SponsoredTeam`.
- If the user didn't enter "Y":
  - Create a `SoccerTeam` object using a team number and the team name that you gathered. The same logic applies as with `SponsoredTeam` except `SoccerTeam` does NOT have a `sponsor_name` instance variable.
- Store your `SoccerTeam` and `SponsoredTeam` objects in a data structure of your choice.

### 3.1 Play games against any 2 teams you choose
Now, you should print out the team number and team name of each team (whether `SoccerTeam` or `SponsoredTeam`) like this:
  - `<team number>: <team name>`
  - For example, with teams of BYU, UVU and Utah State it would look like:
    - ```
        1: BYU
        2: UVU
        3: Utah State
      ```
Followed by asking the user:
- `Enter the team number of the HOME team or enter "exit" to end the season: `
- The user should enter in the number of the team they want to be the home team for the game (for example, using the names shown above, if I enter 2, then UVU would be the home team, etc.)

Then, ask the user:
- `Enter the team number of the AWAY team or enter "exit" to end the season: `
- The user should enter in the number of the away team.

All together, it would look like this (selecting UVU as the Home team and Utah State as the away team):
```
1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 2
Enter the team number of the AWAY team or enter "exit" to end the season: 3
```
In this section, your code must handle 
1. extra white space before or after an input
    - e.g. " 2 " should work the same as "2"
2. input that isn't an integer or a valid team number
    - e.g. if they enter "asdf" or a number that doesn't appear as a team number (like "4" in the above example) then it should print:
        `"Invalid team number! Try again.`
3. inputting the same team number as the home and away team:
  - if the user inputs the same team number for the away and the home team, then it should print:
    - `You can't choose the same team as the home and away team! Try again.`
- If an invalid input is entered, or the same team is entered twice, it should print the message specified above, and then start over by asking the user to enter the number of the home team.

Then, Using the 2 selected team objects, a `Game` object should be created, with a game number (1 for the 1st game played, 2 for the 2nd game played, etc.), as well as the home team object and away team object that will be stored in the `Game` object. See the <a href="#classesrequired">Classes Required</a> section of this document for the necessary instance variables for `Game`.
- The `game_date` instance variable should be a date from the python standard library `datetime`. The date you use doesn't matter, but it should be a different date for each game. I'd recommend just using something like this:
  - put `from datetime import date, timedelta` near or at the top of your python file. This lets you create `date` objects, as well as a `timedelta` that lets you increase or decrease a date by whatever increment you specify. 
  - `self.game_date = date.today() + timedelta(days = <this should equal whatever your self.game_number variable equals>)`
    - this is saying take today's date and add 1 day to it if its the first game, add 2 days to it if it is the second day, etc.

This `Game` object should then call the `play_game` method, described in more detail in section 3.2.

Afterwards, the `Game` object should be stored in a data structure of your choice.

After calling the `play_game` method, it should print out the team numbers and team names again, and gather inputs for the home and away teams, until the user enters `exit` during either the home team input prompt or the away team input prompt. 
- Make sure that it stops asking for inputs/playing games no matter how `exit` is capitalized.
- after `exit` is entered it should print:
  - `The soccer season is over!`

Here's an example of what it would look like playing 2 games and then ending the season (with `play_game` logic written out, which is explained in section 3.2 below)
```
1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 2
Enter the team number of the AWAY team or enter "exit" to end the season: 3

Results of game 1 on 2024-11-03: Home team UVU scored 2 - Away team Utah State scored 3.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 1
Enter the team number of the AWAY team or enter "exit" to end the season: 2

Results of game 2 on 2024-11-04: Home team BYU scored 1 - Away team UVU scored 0.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: exit

The soccer season is over!
```


### 3.2 `play_game` method logic
`play_game` is a method inside the `Game` class that uses the `Game`'s `home_team` and `away_team` instance variables to "play" a soccer game. This method contains most of the same logic from your previous Soccer Teams assignment, but with some differences in how `SponsoredTeam` objects generate their scores.
- Start by generating scores for the home team and the away team using their `generate_score` method, which should just return a random integer between 0 and 3 (inclusive) for `SoccerTeam` objects or an integer between 1 and 3 (inclusive) for `SponsoredTeam` objects using their overridden version (their sponsorship gives them a big, perhaps unrealistic advantage!)
  - Whether the object is a `SoccerTeam` or a `SponsoredTeam`, the object should call `generate_score`. If you wrote your classes correctly (by using inheritance), the correct version of `generate_score` should be automatically chosen when you call the method.
  - No tie scores are allowed. Either regenerate scores if a tie occurs or code the process in a way that ties cannot occur.
- The home and away team scores should be:
  - stored in the `Game` object's instance variables of `home_team_score` and `away_team_score`
  - added to the home and away team objects' `goals_scored` and `goals_allowed` instance variables.
- If the home team score is higher, then record a win for the home team and a loss for the away team and vice versa.
  - Note that in `SoccerTeam` the `wins` and `losses` instance variables need to have a private scope. Meaning you can't directly access those variables in the `Game` class
    - (you can assume you might want to do this to ensure that you never accidentally increase the wins or losses more than you should).
  - So, instead of directly changing the variables, you should write 2 methods in the `SoccerTeam` class: `record_win` (which just increases the `wins` variable by 1) and `record_loss` (which just increases the `losses` variable by 1). In this way, you can affect the `wins` and `losses` variables without having direct access to them. 
- Finally, call the `Game` method `get_game_status` and print the string it returns. The string should look like:
  - `Results of game <game number> on <game date>: Home team <home team name> scored <home team score> - Away team <away team name> scored <away team score>.`
  - For example:
    - `Results of game 1 on 2024-11-03: Home team UVU scored 2 - Away team Utah State scored 3.`
- 

### 4.1 Postseason Menu
After the season ends, you should print out:
```
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program
```
Followed by the input prompt `Enter an option: `

- If the user enters `1` then you go to the Team Info Menu (logic described in section 4.2 below)
- If the user enters `2` then you go to the Game Info Menu (logic described in section 4.3 below)
- If the user enters `exit` then print `Exiting the program.` and the program should end.
- Make sure you can handle extra spaces and different capitalization
  - e.g. " 1 " should work the same as "1", and "EXIT" should be the same as "exit", etc.
- If any other input is given, just print out `Invalid choice! Try again.` and repeat the Postseason menu until a valid input is given.

### 4.2 Team Info Menu
If the user entered `1` in the Postseason Menu, then print out:
- `Team Info Menu:`

Followed by the team number and team name of each `SoccerTeam` or `SponsoredTeam` object you created followed by this message:
- `Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu: `

For example:
```
Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu:  
```
1. Any input should work with leading or trailing spaces.
2. If "exit" is entered (no matter the capitalization) it should go back to the Postseason menu. 
3. If an invalid number or any other invalid option is given, it should print `Invalid team number! Try again.` and show the Team Info Menu again until a valid input is provided.
4. If a valid team number is entered, then it should:
    - run that team's `get_team_info` method and print the result
    - run that team's `get_season_message` method and print the result
    - print out the Team Info Menu again.
    - An example of that is shown below (assuming BYU was selected, and BYU is a `SponsoredTeam` with Cosmo as their sponsor). An explanation of each method is provided after the example output:

```
Team Name: BYU
Season record: 6 - 2 (75%)
Total goals scored: 17 Total goals allowed: 7

Qualified for the NCAA Soccer Tournament! Cosmo is very happy.
```
#### `get_team_info`
`get_team_info` is a method in the `SoccerTeam` class that returns the team name, season record in wins, losses and percent, the total goals scored across all games and the total goals allowed across all games, like this:
```
Team Name: <team name>
Season record: <wins> - <losses> (<season record percent>%)
Total goals scored: <goals scored> Total goals allowed: <goals allowed>
```
For the season record percent, you should use the method `get_record_percentage` in the `SoccerTeam` class. It should just return the number of wins divided by the total number of games played, rounded to the 2nd decimal. In the case that no games have been played, it should just return 0 (normally if no games have been played, it would raise an error because you can't divide by zero). You'll also want to use the `get_record_percentage` method for the `get_season_message` method described below as well. 

#### `get_season_message`
`get_season_message` is a method in the `SoccerTeam` class that returns a message based on the season record of the team that calls it. The logic is identical to the previous soccer teams assignment (a repeat explanation of that logic is given below). However, there is an overridden version in the `SponsoredTeam` class that does the same thing, but adds a statement about how the sponsor feels about the team's performance to the returned message. Here is the logic:

`SoccerTeam` `get_season_message` logic:
- If they won at least 75% of their games, return:
  - `Qualified for the NCAA Soccer Tournament!` 
- If the team won at least 50% but less than 75% then return:
  - `You had a good season.` 
- Otherwise return:
  - `Your team needs to practice!`

<br>

`SponsoredTeam` `get_season_message` logic:
- If they won at least 75% of their games, return:
  - `Qualified for the NCAA Soccer Tournament! <sponsor name> is very happy.` 
- If the team won at least 50% but less than 75% then return:
  - `You had a good season. <sponsor name> hopes you can do better.` 
- Otherwise return:
  - `Your team needs to practice! You are in danger of <sponsor name> dropping you.`

For `SponsoredTeam`, remember that it shouldn't have access to `wins` and `losses` because those are private variables to the `SoccerTeam` class, but it does have access to the `get_record_percentage` method.

### 4.3 Game Info Menu
If the user entered `2` in the Postseason Menu, then print out:
- `Game Info Menu:`

Followed by `Game` and the game number of each `Game` object you created followed by this message:
- `Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: `
For example, if there were 5 games in the season, it would look like this:
```
Game Info Menu:
Game 1
Game 2
Game 3
Game 4
Game 5
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: 
```
1. Any input should work with leading or trailing spaces.
2. If "exit" is entered (no matter the capitalization) it should go back to the Postseason menu. 
3. If an invalid number or any other invalid option is given, it should print `Invalid game number! Try again.` and show the Game Info Menu again until a valid input is provided.
4. If a valid game number is entered, then it should:
    - run that game's `get_game_status` method and print the result
      - `get_game_status` should already have been written in section 3.2 of the instructions, so you shouldn't need to write any new methods for this part.
    - then display the Game Info Menu again.
    
The user should be able to view the info for any Game or Team as many times as they want until they enter "exit" in the Postseason menu.

## Example Output
Here's an example of 3 teams playing 5 games and viewing the info for some teams and games. No invalid input is provided:

```
Enter the number of soccer teams you want to enter (at least 2): 3
Enter a name for team 1: BYU
Enter Y if team 1 is sponsored, otherwise enter N (or anything else): Y
Enter the name of your sponsor: Cosmo 
Enter a name for team 2: UVU
Enter Y if team 2 is sponsored, otherwise enter N (or anything else): N
Enter a name for team 3: Utah State
Enter Y if team 3 is sponsored, otherwise enter N (or anything else): N
1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 1
Enter the team number of the AWAY team or enter "exit" to end the season: 3

Results of game 1 on 2024-11-04: Home team BYU scored 1 - Away team Utah State scored 3.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 3
Enter the team number of the AWAY team or enter "exit" to end the season: 1

Results of game 2 on 2024-11-05: Home team Utah State scored 0 - Away team BYU scored 2.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 1
Enter the team number of the AWAY team or enter "exit" to end the season: 2

Results of game 3 on 2024-11-06: Home team BYU scored 1 - Away team UVU scored 2.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 2
Enter the team number of the AWAY team or enter "exit" to end the season: 3

Results of game 4 on 2024-11-07: Home team UVU scored 2 - Away team Utah State scored 3.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 1
Enter the team number of the AWAY team or enter "exit" to end the season: 2

Results of game 5 on 2024-11-08: Home team BYU scored 1 - Away team UVU scored 2.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: exit

The soccer season is over!
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option: 1

Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu: 1

Team Name: BYU
Season record: 1 - 3 (25%)
Total goals scored: 5 - Total goals allowed: 7

Your team needs to practice! You are in danger of Cosmo dropping you.


Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu: 2   

Team Name: UVU
Season record: 2 - 1 (67%)
Total goals scored: 6 - Total goals allowed: 5

You had a good season.


Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu: exit
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option: 2

Game Info Menu:
Game 1
Game 2
Game 3
Game 4
Game 5
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: 2

Results of game 2 on 2024-11-05: Home team Utah State scored 0 - Away team BYU scored 2.


Game Info Menu:
Game 1
Game 2
Game 3
Game 4
Game 5
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: exit
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option: exit
Exiting the program.
```
Here's a similar example, but with entering invalid inputs at each step to show off the error handling:

```
Enter the number of soccer teams you want to enter (at least 2): asdf
Invalid integer! Try again.

Enter the number of soccer teams you want to enter (at least 2): 1
You must enter an integer of 2 or above. Try again.

Enter the number of soccer teams you want to enter (at least 2): 3
Enter a name for team 1: BYU
Enter Y if team 1 is sponsored, otherwise enter N (or anything else): Y
Enter the name of your sponsor: Cosmo
Enter a name for team 2: UVU
Enter Y if team 2 is sponsored, otherwise enter N (or anything else): asdf
Enter a name for team 3: Utah State
Enter Y if team 3 is sponsored, otherwise enter N (or anything else): N
1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: asdf
Invalid team number! Try again.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 1
Enter the team number of the AWAY team or enter "exit" to end the season: 1
You can't choose the same team as the home and away team! Try again.
1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 1
Enter the team number of the AWAY team or enter "exit" to end the season: 2

Results of game 1 on 2024-11-04: Home team BYU scored 2 - Away team UVU scored 3.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 2
Enter the team number of the AWAY team or enter "exit" to end the season: 1

Results of game 2 on 2024-11-05: Home team UVU scored 0 - Away team BYU scored 2.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 1
Enter the team number of the AWAY team or enter "exit" to end the season: 2

Results of game 3 on 2024-11-06: Home team BYU scored 1 - Away team UVU scored 2.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 1
Enter the team number of the AWAY team or enter "exit" to end the season: 3

Results of game 4 on 2024-11-07: Home team BYU scored 1 - Away team Utah State scored 2.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 2
Enter the team number of the AWAY team or enter "exit" to end the season: 3

Results of game 5 on 2024-11-08: Home team UVU scored 2 - Away team Utah State scored 0.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: EXIT 

The soccer season is over!
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option: asdf
Invalid choice! Try again.
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option: 1

Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu: asdf
Invalid team number! Try again.


Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu: 3

Team Name: Utah State
Season record: 1 - 1 (50%)
Total goals scored: 2 - Total goals allowed: 3

You had a good season.


Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu:       ExIT
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option: 2

Game Info Menu:
Game 1
Game 2
Game 3
Game 4
Game 5
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: asdf
Invalid game number! Try again.


Game Info Menu:
Game 1
Game 2
Game 3
Game 4
Game 5
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: 45
Invalid game number! Try again.


Game Info Menu:
Game 1
Game 2
Game 3
Game 4
Game 5
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: 2

Results of game 2 on 2024-11-05: Home team UVU scored 0 - Away team BYU scored 2.


Game Info Menu:
Game 1
Game 2
Game 3
Game 4
Game 5
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: EXit
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option: exiT
Exiting the program.
```

## Rubric
This assignment contains the automated tests listed below. The tests will ignore spacing, capitalization, and punctuation, but you will fail the tests if you spell something wrong or calculate something incorrectly.

After this table, see the Test Cases table below to see what inputs will be run for each of the tests below. To receive points for a test, the test must pass each of the individual test cases.

<table border="1" style="width: 100%; text-align: center;">
<thead style="text-align: center;">
    <tr>
        <th style="text-align: center;">Test</th>
        <th style="text-align: center;">Test Cases Used </th>
        <th style="text-align: center;">Description</th>
        <th style="text-align: center;">Points</th>
    </tr>
</thead>
<tbody>
    <tr style="text-align: left">
        <td>1. Printed Messages</td>
        <td>1</td>
        <td>
        Your printed output must contain these phrases, but order doesn't matter. Some test cases won't produce all of these printed messages, so just check the test cases table below this if you fail during a specific test case. You will not be docked if you print out any extra statements not included here:
        <ul>
          <li><code>Charmander - Type: Fire - Hit Points: 55</code></li>
          <li><code>Charmander has been healed to 70 hit points.</code></li>
          <li><code>Charmander - Type: Fire - Hit Points: 70</code></li>
          <li><code>Bulbasaur - Type: Grass - Hit Points: 60</code></li>
          <li><code>Squirtle - Type: Water - Hit Points: 65</code></li>
          <li><code>Generated attack value: &lt;number&gt;</code></li>
        </ul>
        Additionally, during each run of your code, exactly <code>3</code> of the following statements must run, no more or less:
          <ul>
            <li><code>Quick Attack (Type: Normal): 6 to 25 Attack Points</code></li>
            <li><code>Tackle (Type: Normal): 5 to 20 Attack Points</code></li>
            <li><code>Flamethrower (Type: Fire): 5 to 30 Attack Points</code></li>
            <li><code>Ember (Type: Fire): 10 to 20 Attack Points</code></li>
            <li><code>Hydro Pump (Type: Water): 20 to 25 Attack Points</code></li>
            <li><code>Solar Beam (Type: Grass): 18 to 27 Attack Points</code></li>
            <li><code>Slash (Type: Normal): 10 to 30 Attack Points</code></li>
            <li><code>Vine Whip (Type: Grass): 10 to 25 Attack Points</code></li>
            <li><code>Water Gun (Type: Water): 5 to 15 Attack Points</code></li>
          </ul>        
        </td>
        <td>9</td>
    </tr>
    <tr>
        <td>2. Pokemon Class</td>
        <td>1</td>
        <td style="text-align: left">
          This test will create Pokemon objects using the arguments shown below. The object should contain the instance variables listed in the expected values column.
          <table border="1">
            <thead>
                <tr>
                    <th>initial arguments</th>
                    <th>expected values</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>'Bulbasaur', 'Grass', 60</code></td>
                    <td><code>'Bulbasaur': str, 'Grass': str, 60: (int, float)</code></td>
                </tr>
                <tr>
                    <td><code>'Charmander', 'Fire', 55</code></td>
                    <td><code>'Charmander': str, 'Fire': str, 55: (int, float)</code></td>
                </tr>
            </tbody>
          </table>
        </td>
        <td>15</td>
    </tr>
    <tr>
        <td>3. Move Class</td>
        <td>1</td>
        <td style="text-align: left">
          This test will create Move objects using the arguments shown below. The object should contain the instance variables listed in the expected values column.
          <table border="1">
            <thead>
                <tr>
                    <th>initial arguments</th>
                    <th>expected values</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>'Tackle', 'Normal', 5, 20</code></td>
                    <td><code>'Tackle': str, 'Normal': str, 5: (int, float), 20: (int, float)</code></td>
                </tr>
                <tr>
                    <td><code>'Water Gun', 'Water', 5, 15</code></td>
                    <td><code>'Water Gun': str, 'Water': str, 5: (int, float), 15: (int, float)</code></td>
                </tr>
            </tbody>
          </table>
        </td>
        <td>15</td>
    </tr>
      <tr>
        <td>4. Pokemon - get info</td>
        <td>1</td>
        <td style="text-align: left">
          This test will use the Pokemon objects created in test 2.
          <table border="1">
            <thead>
                <tr>
                    <th>arguments</th>
                    <th>expected return value</th>
                    <th>expected object update</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>self</code></td>
                    <td><code>Bulbasaur - Type: Grass - Hit Points: 60</code></td>
                    <td><code>None</code></td>
                </tr>
                <tr>
                    <td><code>self</code></td>
                    <td><code>Charmander - Type: Fire - Hit Points: 55</code></td>
                    <td><code>None</code></td>
                </tr>
            </tbody>
          </table>
        </td>
        <td>15</td>
    </tr>
          <tr>
        <td>5. Pokemon - heal</td>
        <td>1</td>
        <td style="text-align: left">
          This test will use the Pokemon objects created in test 2.
          <table border="1">
            <thead>
                <tr>
                    <th>arguments</th>
                    <th>expected return value</th>
                    <th>expected object update</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>self</code></td>
                    <td><code>None</code></td>
                    <td><code>'intial_value': 60, 'final_value': 75</code></td>
                </tr>
                <tr>
                    <td><code>self</code></td>
                    <td><code>None</code></td>
                    <td><code>'intial_value': 55, 'final_value': 70</code></td>
                </tr>
            </tbody>
          </table>
        </td>
        <td>15</td>
    </tr>
    <td>6. Move - get_info</td>
        <td>1</td>
        <td style="text-align: left">
          This test will use the Move objects created in test 3.
          <table border="1">
            <thead>
                <tr>
                    <th>arguments</th>
                    <th>expected return value</th>
                    <th>expected object update</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>self</code></td>
                    <td><code>Tackle (Type: Normal): 5 to 20 Attack Points</code></td>
                    <td><code>None</code></td>
                </tr>
                <tr>
                    <td><code>self</code></td>
                    <td><code>Water Gun (Type: Water): 5 to 15 Attack Points</code></td>
                    <td><code>None</code></td>
                </tr>
            </tbody>
          </table>
        </td>
        <td>15</td>
    </tr>
       <td>7. Move - generate attack value</td>
        <td>1</td>
        <td style="text-align: left">
          This test will use the Move objects created in test 3.
          <table border="1">
            <thead>
                <tr>
                    <th>arguments</th>
                    <th>expected return value</th>
                    <th>expected object update</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>self</code></td>
                    <td><code>(5, 20)</code></td>
                    <td><code>None</code></td>
                </tr>
                <tr>
                    <td><code>self</code></td>
                    <td><code>(5, 15)</code></td>
                    <td><code>None</code></td>
                </tr>
            </tbody>
          </table>
        </td>
        <td>15</td>
    </tr>
        <tr>
        <td>8. Sufficient Comments</td>
        <td>None</td>
        <td style="text-align: left">Your code must include at least <code>10</code> comments. You can use any form of commenting:
        <ul>
          <li><code>#</code></li> 
          <li><code>''' '''</code></li>
          <li><code>""" """</code></li>
        </ul>
        </td>
        <td>1</td>
    </tr>
    <tr>
        <td colspan="3">Total Points</td>
        <td>100</td>
  </tr>
</tbody>
</table>

<br><br>


## Test Cases Summary
<table>
  <tr>
    <th>Test Case Description</th>
    <th>Inputs</th>
  </tr>
  <tr>
    <td><a href="#testcase1">1: Default run</a></td>
    <td><ul>
  <li><code></code></li>
</ul></td>
  </tr>
</table>

<h3 id="testcase1">Test Case 1 Details - Default run</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code></code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Press enter to continue...</code></li>
</ul></td>
  </tr>

  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>Flamethrower (Type: Fire): 5 to 30 Attack Points</code></li>
  <li><code>Generated attack value: &lt;number&gt;</code></li>
  <li><code>Tackle (Type: Normal): 5 to 20 Attack Points</code></li>
  <li><code>Vine Whip (Type: Grass): 10 to 25 Attack Points</code></li>
  <li><code>Solar Beam (Type: Grass): 18 to 27 Attack Points</code></li>
  <li><code>Ember (Type: Fire): 10 to 20 Attack Points</code></li>
  <li><code>Charmander - Type: Fire - Hit Points: 55</code></li>
  <li><code>Charmander has been healed to 70 hit points.</code></li>
  <li><code>Charmander - Type: Fire - Hit Points: 70</code></li>
  <li><code>Bulbasaur - Type: Grass - Hit Points: 60</code></li>
  <li><code>Squirtle - Type: Water - Hit Points: 65</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Flamethrower (Type: Fire): 5 to 30 Attack Points
Generated attack value: 21
Tackle (Type: Normal): 5 to 20 Attack Points
Generated attack value: 14
Vine Whip (Type: Grass): 10 to 25 Attack Points
Generated attack value: 11
Press enter to continue...
Charmander - Type: Fire - Hit Points: 55
Charmander has been healed to 70 hit points.
Charmander - Type: Fire - Hit Points: 70
Bulbasaur - Type: Grass - Hit Points: 60
Charmander - Type: Fire - Hit Points: 70
Squirtle - Type: Water - Hit Points: 65
```

