# Test Case 2

## Description
3 teams, 1 sponsored, 5 games, but with different capitalization, leading and trailing spaces

## Inputs
The inputs below (without the quotes) will be entered one by one each time an `input()` function is found in your code.
```
1: "  3  "
2: "BYU"
3: "  y"
4: "Cosmo"
5: "UVU"
6: "  N"
7: "Utah State"
8: "n"
9: "   2  "
10: " 1  "
11: "3"
12: "1"
13: "1"
14: "3"
15: "2"
16: "1"
17: "1"
18: "3"
19: " EXIT "
20: " 1 "
21: " 1 "
22: " EXIT"
23: "2  "
24: "  3"
25: " eXiT"
26: "EXit  "
```

## Example Output
This is what your terminal should look like if you use the inputs above when running your code.
```
Enter the number of soccer teams you want to enter (at least 2):   3  
Enter a name for team 1: BYU
Enter Y if team 1 is sponsored, otherwise enter N (or anything else):   y
Enter the name of your sponsor: Cosmo
Enter a name for team 2: UVU
Enter Y if team 2 is sponsored, otherwise enter N (or anything else):   N
Enter a name for team 3: Utah State
Enter Y if team 3 is sponsored, otherwise enter N (or anything else): n
1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season:    2  
Enter the team number of the AWAY team or enter "exit" to end the season:  1  

Results of game 1 on 2024-11-05: Home team UVU scored 3 - Away team BYU scored 1.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 3
Enter the team number of the AWAY team or enter "exit" to end the season: 1

Results of game 2 on 2024-11-06: Home team Utah State scored 0 - Away team BYU scored 1.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 1
Enter the team number of the AWAY team or enter "exit" to end the season: 3

Results of game 3 on 2024-11-07: Home team BYU scored 2 - Away team Utah State scored 0.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 2
Enter the team number of the AWAY team or enter "exit" to end the season: 1

Results of game 4 on 2024-11-08: Home team UVU scored 0 - Away team BYU scored 2.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 1
Enter the team number of the AWAY team or enter "exit" to end the season: 3

Results of game 5 on 2024-11-09: Home team BYU scored 3 - Away team Utah State scored 0.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season:  EXIT 

The soccer season is over!
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option:  1 

Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu:  1 

Team Name: BYU
Season record: 4 - 1 (80%)
Total goals scored: 9 - Total goals allowed: 3

Qualified for the NCAA Soccer Tournament! Cosmo is very happy.


Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu:  EXIT
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
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu:   3

Results of game 3 on 2024-11-07: Home team BYU scored 2 - Away team Utah State scored 0.


Game Info Menu:
Game 1
Game 2
Game 3
Game 4
Game 5
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu:  eXiT
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option: EXit  
Exiting the program.
```
