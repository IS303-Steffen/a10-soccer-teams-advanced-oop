# Test Case 1

## Description
3 teams, 1 sponsored, 5 games, viewing multiple teams and games

## Inputs
The inputs below (without the quotes) will be entered one by one each time an `input()` function is found in your code.
```
1: "3"
2: "BYU"
3: "Y"
4: "Cosmo"
5: "UVU"
6: "N"
7: "Utah State"
8: "N"
9: "1"
10: "2"
11: "2"
12: "1"
13: "3"
14: "1"
15: "2"
16: "3"
17: "3"
18: "2"
19: "exit"
20: "1"
21: "1"
22: "2"
23: "3"
24: "exit"
25: "2"
26: "1"
27: "3"
28: "exit"
29: "exit"
```

## Example Output
This is what your terminal should look like if you use the inputs above when running your code.
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
Enter the team number of the AWAY team or enter "exit" to end the season: 2

Results of game 1 on 2024-11-05: Home team BYU scored 1 - Away team UVU scored 0.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 2
Enter the team number of the AWAY team or enter "exit" to end the season: 1

Results of game 2 on 2024-11-06: Home team UVU scored 2 - Away team BYU scored 1.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 3
Enter the team number of the AWAY team or enter "exit" to end the season: 1

Results of game 3 on 2024-11-07: Home team Utah State scored 1 - Away team BYU scored 3.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 2
Enter the team number of the AWAY team or enter "exit" to end the season: 3

Results of game 4 on 2024-11-08: Home team UVU scored 1 - Away team Utah State scored 2.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 3
Enter the team number of the AWAY team or enter "exit" to end the season: 2

Results of game 5 on 2024-11-09: Home team Utah State scored 0 - Away team UVU scored 1.

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
Season record: 2 - 1 (67%)
Total goals scored: 5 - Total goals allowed: 3

You had a good season. Cosmo hopes you can do better.


Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu: 2

Team Name: UVU
Season record: 2 - 2 (50%)
Total goals scored: 4 - Total goals allowed: 4

You had a good season.


Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu: 3

Team Name: Utah State
Season record: 1 - 2 (33%)
Total goals scored: 3 - Total goals allowed: 5

Your team needs to practice!


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
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: 1

Results of game 1 on 2024-11-05: Home team BYU scored 1 - Away team UVU scored 0.


Game Info Menu:
Game 1
Game 2
Game 3
Game 4
Game 5
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: 3

Results of game 3 on 2024-11-07: Home team Utah State scored 1 - Away team BYU scored 3.


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
