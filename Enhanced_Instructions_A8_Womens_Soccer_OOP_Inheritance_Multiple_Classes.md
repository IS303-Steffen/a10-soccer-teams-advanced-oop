Instructions – A8 – Women’s Soccer – OOP Inheritance & Multiple Classes

Overview:
This assignment builds on the past Women’s Soccer assignment, but now soccer teams are stored as objects, and you create objects for games (which each store a home team and away team object). To practice the OOP concept of inheritance, you will create two types of soccer teams: regular teams and sponsored teams. Sponsored teams will inherit from regular soccer teams, but they have sponsors which gives them some advantages.

Libraries Required:
random

Classes Required:
SoccerTeam
Instance Variables:
team_name: (string) name of the team
wins: (int) stores the number of wins
losses: (int) stores the number of losses
goals_scored: (int) the total number goals they have scored across all games
goals_allowed: (int) the total number of goals other teams scored on them across all games
Methods
__init__
The constructor
display_summary_info
prints or returns info on the team and their performance.
generate_score
returns a randomly generated score between 0 and 5
get_season_message
returns a message based on the team’s win rate.
SponsoredTeam (inherits from SoccerTeam)
Instance Variables:
All of the instance variables from SoccerTeam through the use of super()
sponsor_name: (string) the name of the sponsor for the team
Methods
__init__
The constructor. Should call the SoccerTeam constructor.
generate_score
Overrides the SoccerTeam version. Returns a randomly generated score between 1 and 5
get_season_message
Overrides the SoccerTeam version. Returns a message based on the team’s win rate, and also mentions how the sponsor feels about their performance.
Game
Instance variables:
home_team: (Soccer/Sponsored Team) team object of the home team.
away_team: (Soccer/Sponsored Team) team object of the away team.
home_team_score: (integer) how many points the home team scored during the game.
away_team_score: (integer) how many points the away team scored during the game.
Methods:
__init__
The constructor
get_game_status
returns or prints a string with how many points the home and away teams scored and the team names.

Logical Flow:

Ask for the name of your home team (like “BYU”)

Then, ask for the name of the home team’s sponsor. Or if they aren’t sponsored, tell the user to enter “N”:

If they enter anything other than “N”, create a SponsoredTeam object for the home team, using the inputted text as the sponsor_name. Otherwise if they entered “N” make a regular SoccerTeam object.
Then, ask for the number of games your home team will play in their season (Advice: I recommend keeping the number pretty low, like 2 games, when testing it so it is quicker to test).

Then, for each game that your home team will play:
Ask the name of the away team (e.g. “Utah State”) and include which number game this will be for. For example, for the first game it would look like:
“Enter the name of the away team for game 1: “

For the second game, it would look like:
Enter the name of the away team for game 2:
And so on
After entering in the away team name, create either a regular SoccerTeam object for the team or a SponsoredTeam. Make it a 50/50 chance for which type of object they are. If you make a Sponsored team, just use “Opponent Sponsor” as sponsor_name.
Now, randomly generate scores for both the home team object and the away team object. To do this, use the generate_score method in the SoccerTeam/SponsoredTeam class.  The generate_score method should return a randomly generated score. For SoccerTeam the score should be between 0 and 5 (inclusive), but for a SponsoredTeam, you should have another version of generate_score that generates a random score between 1 and 5 (inclusive). 
In the case that there is a tie between the home and the away teams, keep generating new scores for the home and away teams until there isn’t a tie.
For both the home team object and the away team object, update the following instance variables:
goals_scored, goals_allowed, wins, and losses.
goals_scored and goals_allowed should store a running count of the total number of goals the team has scored or allowed across the season, not just for an individual game.
Additionally, create a Game object using the home team object, the away team object, the home team’s score for that game, and the away team’s score for that game. The game object should be stored in a list, so that the games can be looked up at the end of your program.
Print out the name of the home team’s name and their score, as well as the away team’s name and their score. If the away team’s name were “UVU” it might look this this:
“BYU's score: 3 UVU's score: 1”
Do the above steps of this section however many times the user inputted for the number of games the home team would play in the season. (E.g. if they inputted 3 for the number of games, go through the above logic 3 times). For full credit, you must use a loop to do this. A for loop is probably easier in this situation, but a while loop could work too.
Once the season is over (all games played) run the following methods on the home team object:
display_summary_info
This should print out (or return, it’s up to you) the team’s name, their season record (number of wins followed by number of losses), and the total number of goals they scored and the total number of goals they allowed.

This method should only appear in the SoccerTeam class, but since SponsoredTeam will inherit from SoccerTeam, it should also have access to it.
get_season_message
This should print out (or return, it’s up to you) a message based on the team’s performance
If they won at least 75% of their games, then print out “Qualified for the NCAA Women's Soccer Tournament”.
If the team won at least 50% but less than 75% then print out “You had a good season”.
Otherwise print out “Your team needs to practice!”.
Additionally, if the team is a SponsoredTeam, there should be an overridden version of get_season_message that also adds a statement about how the sponsor feels about the performance. After the statements already shown above, you would add:
If they won at least 75% of their games, then also add “{sponsor name} is very happy.”
If the team won at least 50% but less than 75% then also add “But {sponsor name} hopes you can do better.”
Otherwise also add “You are in danger of {sponsor name} dropping you.”
For example, if a sponsored team (with the sponsor “Rich Co.”) won less than 50% of their games, it would display:

Now, continually ask the user to either enter in a number between 1 and the total number of games played to see stats about that game, or to enter exit.

If they enter in a valid number, run the get_game_status method on that game object (you should be able to access it if you stored each game object in a list while you were looping through each game previously).
get_game_status should either print or return a message with the home team name, what they scored in that game, and the away team name with what they scored in that game.

The user should continually be asked to enter a number until they enter “exit”, at which point the program will end.

None of the methods can reference global variables.

You are not required to catch exceptions, meaning you can expect the user to provide valid inputs. However, feel free to practice catching exceptions or using defensive programming to make the program run more smoothly. 

Upload just the python file to Learning Suite. This means you should upload the .py file that you made. You will lose points if you copy/paste your code directly to Learning Suite, or upload something like a word file instead of the .py file.

Example Output:

	












Rubric:

