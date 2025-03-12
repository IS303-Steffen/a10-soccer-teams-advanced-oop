#### Assignment 10
# Soccer Teams Inheritance

This assignment uses some of the logic from the previous Soccer Teams assignment, but adds in these concepts:
- OOP
    - association
    - inheritance
    - private variables
- error handling.

Now you'll create `Game` objects that store a home team and away team object. Teams can be regular `SoccerTeam` objects or `SponsoredTeam` objects with modified behavior. Any 2 teams can "play" as many games as they want, all while storing data about the games and teams in their objects. After all games have been played the user can view all the data from any team or any game.

Coding all this requires much more work setting everything up compared to the previous Soccer Teams assignment, but hopefully this assignment demonstrates how storing data inside objects allows for far more complex interactions (imagine storing all this data in individual variables or other data structures)

#### Reminder on what to do if you fail a test:
Remember that if you fail a specific test during a specific input test case, you can see the details of that input test case by going into the `descriptions_of_test_cases` folder. I recommend opening up the file of the input test case you are failing, and then running your code using the exact same set of inputs shown there to help figure out why you might not be passing a test.

## Libraries Required:
- `random`
- `datetime`
    - add `from datetime import date, timedelta` near the top of your code.

## Classes Required
I summarize the structure of the classes you'll need to write in the file `Classes_Required.md` to save space in this document. However, I recommend you just start with the "Logical Flow" section of the instructions and create/update your classes as you go, rather than trying to write all your classes before any of the other logic. But do whatever feels natural to you.

### IMPORTANT:
Please use the same capitalization case as what is shown in these instructions for all the class names and variables, otherwise the automated tests might break. For example, please call your class `SoccerTeam`, NOT `soccerTeam` or `soccer_team`, etc. I'll try and improve the automated tests in a future semester to account for alternate spellings. Sorry for any annoyance that causes you.

## Logical Flow:
For this assignment, you will need to handle improper inputs to receive full credit. You can do it using exception handling or a defensive coding style, whatever you prefer. If you prefer a more defensive style of coding, you might find the `isdecimal()` string method useful to tell whether an input is an integer or not. <a href="https://chatgpt.com/share/6725552e-5bdc-8009-8b23-ab682e98f965" target="_blank">Click here for an example of how it is used.</a>

### 1: Ask for the number of soccer teams to create
Ask the user:
- `Enter the number of soccer teams you want to enter (at least 2): `

Make sure your code can handle:
1. extra white space before or after an input
    - e.g. `" 2 "` should work the same as `"2"`
2. input that isn't an integer
    - e.g. if they enter `"asdf"` it should print:
        `Invalid integer! Try again.`
3. input that is under 2:
    - e.g. if they enter 1, 0, or a negative number, it should print:
        `You must enter an integer of 2 or above. Try again.`
- If an invalid integer or an integer under 2 is provided, you must ask continually ask the user to enter the number of soccer teams again until a valid input is provided.

### 2: Create the `SoccerTeam` or `SponsoredTeam` objects
For the number of teams that the user enters in the previous section, do the following:
- Ask the user:
    - `Enter a name for team <team number>: `
    - So, if it is the first team you are making it would be:
        - `Enter a name for team 1: `, etc.
- Then, ask the user:
    - `Enter Y if team <team_number> is sponsored, otherwise enter N (or anything else): `
    - Make sure this will work even if the user enters a lower case "y" or enters it with extra spaces. So `"y"`, `" y "`, `" Y"`, and `"Y"` should all work.
- If the user did NOT enter `"Y"` (or its accepted variations):
  - Create a `SoccerTeam` object using a team number and the team name that you gathered. You should only need to pass in the team number and team name as arguments when creating the object. Team number should be `1` for the 1st team created, `2` for the 2nd, etc. Also, please spell the class name exactly as `SoccerTeam` or the automated tests may not work. These are all the instance variables that your `SoccerTeam` class should have:
    - Instance Variables:
      - `team_number`: (int) the number (1, 2, 3, etc.) of the team.
      - `team_name`: (str) name of the team.
      - `wins`: (int) stores the number of wins. Defaults to 0. It MUST be a private variable (meaning it shouldn't just be called "wins").
      - `losses`: (int) stores the number of losses. Defaults to 0. It MUST be a private variable (meaning it shouldn't just be called "losses").
      - `goals_scored`: (int) the total number goals they have scored across all games. Defaults to 0.
      - `goals_allowed`: (int) the total number of goals other teams scored on them across all games. Defaults to 0.
- If the user DID enter `"Y"` (or its accepted variations) then ask:
    - `Enter the name of your sponsor: `
    - Store the sponsor name that is entered.
    - Create a `SponsoredTeam` object using a team number, team name, and sponsor name as arguments. The `SponsoredTeam` class must inherit from `SoccerTeam`. Also, please spell the class name exactly as `SponsoredTeam` or the automated tests may not work.`SponsoredTeam` objects will have the exact same instance variables as `SoccerTeam`, in addition to an extra instance variable:
      - `sponsor_name`: (str) the name of the sponsor for the team.
- Be sure to store your `SoccerTeam` and `SponsoredTeam` objects in a data structure of your choice.

### 3.1: Select any 2 teams and create a `Game` object
Now, you should print out the team number and team name of each team (whether it's a `SoccerTeam` or `SponsoredTeam`) like this:
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
In this section, your code must handle:
1. extra white space before or after an input
    - e.g. `" 2 "` should work the same as `"2"`
2. input that isn't an integer or a valid team number
    - e.g. if they enter `"asdf"` or a number that doesn't appear as a team number (like `"4"` in the above example) then it should print:
        `"Invalid team number! Try again.`
3. inputting the same team number as the home and away team:
  - if the user inputs the same team number for the away and the home team, then it should print:
    - `You can't choose the same team as the home and away team! Try again.`

If an invalid input is entered, or the same team is entered twice, it should print one of the corresponding message specified above, and then start over by asking the user to enter the number of the home team.

Then, using the 2 selected team objects, create a `Game` object. When creating a `Game` object, the arguments should include a game number (1 for the 1st game played, 2 for the 2nd game played, etc.), as well as the home team object and away team object. These are all the instance variables that your `Game` class should have:
- Instance variables:
    - `game_number`: (int) the number of the game (1, 2, 3, etc.).
    - `game_date`: (date) the date the game was played.
    - `home_team`: (Soccer/Sponsored Team) team object of the home team.
    - `away_team`: (Soccer/Sponsored Team) team object of the away team.
    - `home_team_score`: (int) how many points the home team scored during the game. Defaults to 0.
    - `away_team_score`: (int) how many points the away team scored during the game. Defaults to 0.
- The `game_date` instance variable should be a date from the python standard library `datetime`. The date you use doesn't matter, but it should be a different date for each game. I'd recommend just using something like this:
  - put `from datetime import date, timedelta` at the top (or close to the top) of your python file. This lets you create `date` objects, as well as a `timedelta` that lets you increase or decrease a date by whatever increment you specify.
  - Then, in your `Game` constructor where you make the `game_date` instance variable, you could use code like this:
    - `self.game_date = date.today() + timedelta(days = self.game_number)`
    - This code will get today's date and add 1 day to it if its the first game, add 2 days to it if it is the second day, etc.

This `Game` object should then call the `play_game` method.

### 3.2: `play_game` Method logic
`play_game` is a method inside the `Game` class that uses the `Game`'s `home_team` and `away_team` instance variables to "play" a soccer game. This method contains most of the same logic from your previous Soccer Teams assignment, but with some differences in how `SponsoredTeam` objects generate their scores.
1. Generate scores for the home and away team.
    - Start by generating scores for the home team and the away team using their `generate_score` method, which should appear in both of the `SoccerTeam` and `SponsoredTeam` classes. `generate_score` must just return a random integer between 0 and 3 (inclusive) for `SoccerTeam` objects, or an integer between 1 and 3 (inclusive) for `SponsoredTeam` objects using their overridden version (their sponsorship gives them a big, perhaps unrealistic advantage!)
    - Whether the object is a `SoccerTeam` or a `SponsoredTeam`, the object should call `generate_score`. If you wrote your classes correctly (by using inheritance), the correct version of `generate_score` should be automatically chosen when you call the method.
    - No tie scores are allowed. Either regenerate scores if a tie occurs or code the process in a way that ties cannot occur.
2. Store the home and away team's scores:
    - Store the home team's score in the `Game` object's instance variable of `home_team_score`. Do the same for the away team's score in the `away_team_score` instance variable.
3. Increase the `goals_scored` and `goals_allowed` of each team.
    - Add the to the home and away team objects' `goals_scored` and `goals_allowed` instance variables.
4. If the home team score is higher, then record a win for the home team and a loss for the away team and vice versa.
    - You record wins/losses in the `wins` or `losses` instance variables in the `SoccerTeam` / `SponsoredTeam` objects.
    - Remember that you should have made the `wins` and `losses` instance variables have a private scope. Meaning you can't directly access those variables in the `Game` class.
      - (As for why you would ever do this, you can assume you might want to ensure that you never accidentally increase the wins or losses more than you should).
    - So, instead of directly changing the variables, you should write 2 methods in the `SoccerTeam` class: `record_win` (which just increases the `wins` variable by 1) and `record_loss` (which just increases the `losses` variable by 1). In this way, you can affect the `wins` and `losses` variables without having direct access to them. Call each of those methods inside the `play_game` method (which one you call for which team depends on whose score was higher)
5. Display game status results
    - Finally, call the `Game` method `get_game_status` and print the string it returns. The only thing that `get_game_status` does is return a string. The string should look like:
      - `Results of game <game number> on <game date>: Home team <home team name> scored <home team score> - Away team <away team name> scored <away team score>.`
    - For example:
      - `Results of game 1 on 2024-11-03: Home team UVU scored 2 - Away team Utah State scored 3.`
    - The date should appear in the format of year-month-day (which should happen automatically if you used the date.today() code shown in the instructions earlier)

### 3.3: Continue selecting teams for more games

After calling the `play_game` method, The `Game` object that called the method should be stored in a data structure of your choice.

Then, begin the process of gathering home and away teams again by printing out the team numbers and team names again, and asking for inputs for the home and away teams, until the user enters `exit`. Note that the user should be able to enter `exit` during either the home team input prompt or the away team input prompt, so make sure it works in either situation.
- Make sure that it stops asking for inputs/playing games no matter how `exit` is capitalized, and if there are leading or trailing spaces. For example `" EXIT "` should work the same as `"exit"`

after `exit` is entered it should print:
  - `The soccer season is over!`

Here's an example of what it would look like playing 2 games and then ending the season.

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

### 4.1: Postseason Menu
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
  - e.g. `" 1 "` should work the same as `"1"`, and `" EXIT "` should be the same as `"exit"`, etc.
- If any other input is given, just print out `Invalid choice! Try again.` and repeat the Postseason menu until a valid input is given.

### 4.2: Team Info Menu
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
2. If "exit" is entered (no matter the capitalization) it should go back to the Postseason menu. Make sure it goes back to the Postseason menu, entering "exit" here SHOULD NOT END THE PROGRAM.
3. If an invalid number or any other invalid option is given, it should print `Invalid team number! Try again.` and show the Team Info Menu again until a valid input is provided.
4. If a valid team number is entered, then it should:
    - run that team's `get_team_info` method (described below) and print the result
    - run that team's `get_season_message` method (described below) and print the result
    - print out the Team Info Menu again.
    - An example of that is shown below (assuming BYU was selected, and BYU is a `SponsoredTeam` with Cosmo as their sponsor). An explanation of each method is provided after the example output:

```
Team Name: BYU
Season record: 6 - 2 (75%)
Total goals scored: 17 Total goals allowed: 7

Qualified for the NCAA Soccer Tournament! Cosmo is very happy.
```
#### `get_team_info`
`get_team_info` is a method in the `SoccerTeam` class that *returns* the team name, season record in wins, losses and percent, the total goals scored across all games and the total goals allowed across all games, like this:
```
Team Name: <team name>
Season record: <wins> - <losses> (<season record percent>%)
Total goals scored: <goals scored> Total goals allowed: <goals allowed>
```
For the season record percent part of the string, you should get the value using the method `get_record_percentage` in the `SoccerTeam` class (this is important because you can't directly access `wins` and `losses` in the `SponsoredTeam` class because they are private to the `SoccerTeam` class).
- `get_record_percentage` must return the total number of wins divided by the total number of games played, rounded to the 2nd decimal.
  - For example, if a team has won 1 game and played 2 games total, `get_record_percentage` should return the float `.5`. Any formatting you apply to that would be done after in the `get_team_info` method, not in the `get_record_percentage` method.
  - In the case that no games have been played, it should just return 0 (normally if no games have been played, it would raise an error because you can't divide by zero). You'll also want to use the `get_record_percentage` method for the `get_season_message` method described below as well. 

#### `get_season_message`
`get_season_message` is a method in the `SoccerTeam` class that returns a message based on the season record of the team that calls it. The logic is identical to the previous soccer teams assignment (a repeat explanation of that logic is given below). However, there is also an overridden version of `get_season_message` in the `SponsoredTeam` class that does the same thing, but adds a statement about how the sponsor feels about the team's performance to the returned message. Here is the logic:

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

For `SponsoredTeam`, remember that it shouldn't have access to `wins` and `losses` because those are private variables to the `SoccerTeam` class, but it does have access to the `get_record_percentage` method, which should give you the percentage you need in your if statements.

### 4.3: Game Info Menu
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
2. If "exit" is entered (no matter the capitalization) it should go back to the Postseason menu. Make sure it goes back to the Postseason menu, entering "exit" here SHOULD NOT END THE PROGRAM.
3. If an invalid number or any other invalid option is given, it should print `Invalid game number! Try again.` and show the Game Info Menu again until a valid input is provided.
4. If a valid game number is entered, then it should:
    - run that game's `get_game_status` method and print the result
      - `get_game_status` should already have been written in section 3.2 of the instructions, so you shouldn't need to write any new methods for this part.
    - Then display the Game Info Menu again.
    
The user should be able to view the info for any Game or Team as many times as they want until they enter "exit" in the Postseason menu.

## Grading Rubric
See the Rubric.md file. Remember to right click and select "Open Preview" to see it formatted so it is readable.


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
