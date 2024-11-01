#### Assignment 9
# Soccer Teams Inheritance

This assignment uses some of the logic from the previous Soccer Teams assignment, but adds in:
- OOP
    - association
    - inheritance
    - private variables
- error handling.

Now soccer teams are stored as objects, and you'll create `Game` objects that store a home team and away team object. Teams can now be regular `SoccerTeam` objects or `SponsoredTeam` objects that have some extra and modified behavior. You'll play as many games as you want between any 2 teams that you create, all while storing the team and game objects. You'll then be able to view all the data from any team or any game after you've played through the "season" of games.

This requires much more setup than the previous Soccer Teams assignment, but hopefully this lets you see how objects let you define a structure that you can dynamically interact with in a much fuller way.

## Libraries Required:
- `random`
- `datetime`
    - add `from datetime import date, timedelta` near the top of your code.

## Classes Required:
#### `SoccerTeam`
- Instance Variables:
    - `team_number`: (int) the number (1, 2, 3, etc.) of the team.
    - `team_name`: (str) name of the team
    - `wins`: (int) stores the number of wins. It MUST be a private variable
    - `losses`: (int) stores the number of losses. It MUST be a private variable
    - `goals_scored`: (int) the total number goals they have scored across all games
    - `goals_allowed`: (int) the total number of goals other teams scored on them across all games
- Methods
    - `__init__`
        - The constructor
    - `record_win`
        - adds 1 to the `wins` private variable
    - `record_loss`
        - adds 1 to teh `losses` private variable
    - `get_record_percentage`
        - returns the season record as a percentage (wins / total games played). Needs to handle any potential zero division errors.
    - `get_team_info`
        - returns info on the team and their performance.
    - `generate_score`
        - returns a randomly generated score between 0 and 3
    - `get_season_message`
        - returns a message based on the team’s win rate.
#### `SponsoredTeam` (inherits from `SoccerTeam`)
- Instance Variables:
    - All of the instance variables from SoccerTeam through the use of super()
    - `sponsor_name`: (str) the name of the sponsor for the team
- Methods
    - `__init__`
        - The constructor. Should call the SoccerTeam constructor.
    - `generate_score`
        - Overrides the SoccerTeam version. Returns a randomly generated score between 1 and 5
    - `get_season_message`
        - Overrides the SoccerTeam version. Returns a message based on the team’s win rate, and also mentions how the sponsor feels about their performance.
#### `Game`
- Instance variables:
    - `game_number`: (int) the number of the game (1, 2, 3, etc.).
    - `game_date`: (date) the date the game was played.
    - `home_team`: (Soccer/Sponsored Team) team object of the home team.
    - `away_team`: (Soccer/Sponsored Team) team object of the away team.
    - `home_team_score`: (int) how many points the home team scored during the game.
    - `away_team_score`: (int) how many points the away team scored during the game.
- Methods:
    - `__init__`
        - The constructor
    - `get_game_status`
        - returns or prints a string with how many points the home and away teams scored and the team names.
    - `play_game`
        - generates scores for the home and away team objects, and updates the `Game`'s scores, and the teams' `goals_scored`, `goals_allowed`, `wins`, `losses`, and calls the `get_game_status`

        - `self.game_date = date.today() + timedelta(days=<this should equal whatever your self.game_number variable equals>)`

## Logical Flow:
For this assignment, you will need to handle improper inputs to receive full credit. You can do it using exception handling or a defensive coding style, whatever you prefer. Especially if you prefer a more defensive style of coding, you might find the `isdigit()` method for strings useful if we haven't talked about it in class. <a href="https://chatgpt.com/share/6725552e-5bdc-8009-8b23-ab682e98f965" target="_blank">Click here for an example of how it is used.</a>

### Ask for the number of soccer teams to create
Ask the user:
- `Enter the number of soccer teams you want to enter (at least 2): `
Make sure your code can handle:
- extra white space before or after an input
    - e.g. " 2 " should work the same as "2"
- 


Ask for the name of your home team (like “BYU”)
 
•	Then, ask for the name of the home team’s sponsor. Or if they aren’t sponsored, tell the user to enter “N”:
o	 
o	If they enter anything other than “N”, create a SponsoredTeam object for the home team, using the inputted text as the sponsor_name. Otherwise if they entered “N” make a regular SoccerTeam object.
•	Then, ask for the number of games your home team will play in their season (Advice: I recommend keeping the number pretty low, like 2 games, when testing it so it is quicker to test).
o	 
•	Then, for each game that your home team will play:
o	Ask the name of the away team (e.g. “Utah State”) and include which number game this will be for. For example, for the first game it would look like:
	“Enter the name of the away team for game 1: “
	 
o	For the second game, it would look like:
	Enter the name of the away team for game 2:
	And so on
o	After entering in the away team name, create either a regular SoccerTeam object for the team or a SponsoredTeam. Make it a 50/50 chance for which type of object they are. If you make a Sponsored team, just use “Opponent Sponsor” as sponsor_name.
o	Now, randomly generate scores for both the home team object and the away team object. To do this, use the generate_score method in the SoccerTeam/SponsoredTeam class.  The generate_score method should return a randomly generated score. For SoccerTeam the score should be between 0 and 5 (inclusive), but for a SponsoredTeam, you should have another version of generate_score that generates a random score between 1 and 5 (inclusive). 
	In the case that there is a tie between the home and the away teams, keep generating new scores for the home and away teams until there isn’t a tie.
o	For both the home team object and the away team object, update the following instance variables:
	goals_scored, goals_allowed, wins, and losses.
	goals_scored and goals_allowed should store a running count of the total number of goals the team has scored or allowed across the season, not just for an individual game.
o	Additionally, create a Game object using the home team object, the away team object, the home team’s score for that game, and the away team’s score for that game. The game object should be stored in a list, so that the games can be looked up at the end of your program.
o	Print out the name of the home team’s name and their score, as well as the away team’s name and their score. If the away team’s name were “UVU” it might look this this:
	“BYU's score: 3 UVU's score: 1”
o	Do the above steps of this section however many times the user inputted for the number of games the home team would play in the season. (E.g. if they inputted 3 for the number of games, go through the above logic 3 times). For full credit, you must use a loop to do this. A for loop is probably easier in this situation, but a while loop could work too.
•	Once the season is over (all games played) run the following methods on the home team object:
o	display_summary_info
	This should print out (or return, it’s up to you) the team’s name, their season record (number of wins followed by number of losses), and the total number of goals they scored and the total number of goals they allowed.
	 
	This method should only appear in the SoccerTeam class, but since SponsoredTeam will inherit from SoccerTeam, it should also have access to it.
o	get_season_message
	This should print out (or return, it’s up to you) a message based on the team’s performance
•	If they won at least 75% of their games, then print out “Qualified for the NCAA Women's Soccer Tournament”.
•	If the team won at least 50% but less than 75% then print out “You had a good season”.
•	Otherwise print out “Your team needs to practice!”.
	Additionally, if the team is a SponsoredTeam, there should be an overridden version of get_season_message that also adds a statement about how the sponsor feels about the performance. After the statements already shown above, you would add:
•	If they won at least 75% of their games, then also add “{sponsor name} is very happy.”
•	If the team won at least 50% but less than 75% then also add “But {sponsor name} hopes you can do better.”
•	Otherwise also add “You are in danger of {sponsor name} dropping you.”
	For example, if a sponsored team (with the sponsor “Rich Co.”) won less than 50% of their games, it would display:
•	 
•	Now, continually ask the user to either enter in a number between 1 and the total number of games played to see stats about that game, or to enter exit.
o	 
•	If they enter in a valid number, run the get_game_status method on that game object (you should be able to access it if you stored each game object in a list while you were looping through each game previously).
o	get_game_status should either print or return a message with the home team name, what they scored in that game, and the away team name with what they scored in that game.
o	 
•	The user should continually be asked to enter a number until they enter “exit”, at which point the program will end.

None of the methods can reference global variables.

You are not required to catch exceptions, meaning you can expect the user to provide valid inputs. However, feel free to practice catching exceptions or using defensive programming to make the program run more smoothly. 

Upload just the python file to Learning Suite. This means you should upload the .py file that you made. You will lose points if you copy/paste your code directly to Learning Suite, or upload something like a word file instead of the .py file.





The purpose of this assignment is to practice the syntax of classes and creating objects. This is an individual assignment, but it is preparation for your next project, “P1 – Pokémon Battle”, which is a group project.

You will create 3 `Pokemon` objects, and 9 `Move` objects. If you’ve never heard of or played Pokémon, they are popular fictional creatures that learn “moves” which are attacks or abilities that they perform. Pokémon and moves have elemental types, like “Fire”, “Water”, “Grass”, and “Normal”. 

In this assignment you will just create the objects (with their attributes and methods), and practice putting the objects in lists and accessing their attributes and methods. However, during the group project, you will have the objects interact with each other in a “battle”. You don’t have to have any prior knowledge of Pokémon to do this assignment and the upcoming project, but it may help you to <a href="https://www.youtube.com/clip/Ugkx_pVqGoZu4Vx3ux5fjGtyF28lin6_e-qW">watch this clip</a> for an idea of what Pokémon interactions are like: 

You will put your code in the `a8_pokemon_and_move_classes.py` file. Do not edit or delete any other files.

## Libraries Required:
•	random


## Classes Required:
You can write the class names in PascalCase, camelCase, or snake_case (though PascalCase is the convention for class names in Python). The automated tests will recognize any of those choices. The names of instance variables are not checked by the automated tests (only the values of the variables are checked) so you can name them whatever you want. Method names can also be in snake_case, camelCase, or PascalCase (though snake_case is the convention for method/function names in Python).

For clarity / organization, I've listed out the structure of the classes first before the Logical Flow section, but some of you may prefer to just skip to the Logical Flow section. Choose what feels natural.

#### Move
- Instance Variables:
  - `move_name` (string)
    - the name of the move
  - `elemental_type` (string)
    - will have value of either “Water”, “Fire”,  “Grass”, or “Normal”
  - `low_attack_points` (int)
    - the lowest number of points that can be generated for the move
  - `high_attack_points` (int)
    - the highest number of points that can be generated for the move
- Methods:
  - `__init__`
    - The constructor / initializer!
  - `get_info`
    - returns a string with the move_name, elemental_type, and the low_attack_points and high_attack_points.
  - `generate_attack_value`
    - returns an int of a randomly generated number between the low_attack_points, and the high_attack_points of the move.

#### Pokemon
>Note: name your class `Pokemon` without an accent, instead of `Pokémon`. Sorry to the purists :(
- Instance Variables:
  - `name` (string)
    - the Pokemon’s name
  - `elemental_type` (string)
    - will have value of either “Water”, “Fire”, or “Grass”
  - `hit_points` (integer)
    - represents the health of the pokemon
- Methods:
  - `__init__`
    - The constructor / initializer!
  - `get_info`
    - returns a string with the name, elemental_type and hit_points
  - `heal`
    - adds 15 hit points to `hit_points` and prints out a message with the new number of hit_points.


## Logical Flow:
Note, this program won't store any user input. You'll hardcode all of the values provided in the instructions. This takes some time to write out, but will make it much quicker to run (instead of typing in inputs each run), and you will reuse all the objects you type out in the upcoming project.

### Part 1: Creating Move objects

Moves represent actions that a Pokémon can take. They have a name (like “Tackle”), an elemental type (like “Normal” or “Fire”) that describes the move, as well as a range of damage values that the move can do. For example, a move might do somewhere between 5 and 15 points of damage, so you need to store lower and upper bounds for that.

- Create a Move class
  - Create the constructor with parameters for `self`, `move_name`, `elemental_type`, `low_attack_points`, and `high_attack_points`.
  - Create a method called `get_info` with just `self` as a parameter. It returns a string that includes all of its variables.
    - `<move name> (Type: <move elemental type>): <low attack points> to <high attack points> Attack Points`
    - For example, for the move Tackle, that is a Normal type with attack points between 5 and 20, the returned string should look like:
      - `Tackle (Type: Normal): 5 to 20`
  - Create a method called `generate_attack_value`, with just `self` as a parameter. It will generate a random number between the `low_attack_points` and `high_attack_points` (inclusive on both ends) and return that value.
- Create 9 `Move` objects.
  - Call the constructor 9 times to store 9 different `Move` objects in 9 different variables. The values that you can pass into the constructor are given in each row in the table below:

  - | Move Name      | Elemental Type | Low Attack Points | High Attack Points |
    |----------------|----------------|-------------------|--------------------|
    | Tackle         | Normal         | 5                 | 20                 |
    | Quick Attack   | Normal         | 6                 | 25                 |
    | Slash          | Normal         | 10                | 30                 |
    | Flamethrower   | Fire           | 5                 | 30                 |
    | Ember          | Fire           | 10                | 20                 |
    | Water Gun      | Water          | 5                 | 15                 |
    | Hydro Pump     | Water          | 20                | 25                 |
    | Vine Whip      | Grass          | 10                | 25                 |
    | Solar Beam     | Grass          | 18                | 27                 |

- Create a list that stores each of the 9 objects in it.
- Do a for loop that runs 3 times, and in each iteration, do the following:
  - Randomly select a `Move` object from the list you created
  - Print out the result of the `get_info` method of the randomly selected object.
  - Print out `Generated attack value: ` and then the returned value from running the `generate_attack_value` method on the randomly selected object.
  - Then delete the move from the list of moves.
- After finishing the loop, to add a pause in your program, add this line of code:
  - `input(“Press enter to continue...)`
  - The above code doesn’t store anything, but it makes your program pause until you press enter (or return) on your keyboard. We’ll use the above code more in the future project, but put it here just to get familiar with it. 

### Part 2: Creating Pokémon objects

`Pokemon` objects represent a fictional creature that has a name, an elemental type, and hit points, which is basically a health indicator. A `Pokemon` faints when its hit points reach 0.

- Create a `Pokemon` class
> Note: conventionally, any classes you write go at the top of the Python file. You can put the `Pokemon` class below the other code you wrote to make `Move` objects (and it will still work) but that isn’t how most Python code is usually organized. You can do whatever you want though.
  - Create the constructor with parameters for `self`, `name`, `elemental_type`, and `hit_points`
  - Create a method called `get_info` that returns the `name`, `elemental_type`, and `hit_points` in a string.
    - `<Pokemon name> - Type: <elemental type> - Hit Points: <hit points>`
  - For example for a water type pokemon called Squirtle with 65 hit points the returned string would look like:
    - Squirtle – Type: Water – Hit Points: 65`
  - Create a method called `heal` with just `self` as a parameter. It increases the current value of `hit_points` by 15 and prints out a message with the Pokémon’s `name` and what their new value of `hit_points` are
    - For example, if Squirtle had 65 hit points and the heal method was run on it, it would print:
      - `Squirtle has been healed to 80 hit points.`
- Create 3 `Pokemon` objects
  - Call the constructor 3 times to create 3 different `Pokemon` objects stored in 3 different variables. The values that you can pass into the constructor are given in each row in the table below:

  - | Name        | Elemental Type | Hit Points |
    |-------------|----------------|------------|
    | Bulbasaur   | Grass          | 60         |
    | Charmander  | Fire           | 55         |
    | Squirtle    | Water          | 65         |

- Call the `get_info` method on the object storing the Charmander Pokémon and print out the result
- Then call the heal method on the same Charmander object
- Then call the get_info method on the same Charmander object again and print out the result (you should see that the hit_points have increased)
- Put the 3 `Pokemon` objects into a list
- Loop through the list and print out the result of `get_info` on each `Pokemon` object in the list.

## Example Output:

Note the specific moves that print out will be different each time the program is run since you are randomly selecting them from a list:

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

