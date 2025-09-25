# Test Case 8

## Description
Invalid Game Info Menu option

## Inputs
The inputs below (without the quotes) will be entered one by one each time an `input()` function is found in your code.
```
1: "3"
2: "BYU"
3: "N"
4: "UVU"
5: "N"
6: "Utah State"
7: "N"
8: "3"
9: "1"
10: "1"
11: "2"
12: "exit"
13: "2"
14: "asdf"
15: "4"
16: "exit"
17: "exit"
```

## Example Output
This is what your terminal should look like if you use the inputs above when running your code.
```
Enter the number of soccer teams you want to enter (at least 2): 3
Enter a name for team 1: BYU
Enter Y if team 1 is sponsored, otherwise enter N (or anything else): N
Enter a name for team 2: UVU
Enter Y if team 2 is sponsored, otherwise enter N (or anything else): N
Enter a name for team 3: Utah State
Enter Y if team 3 is sponsored, otherwise enter N (or anything else): N
1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 3
Enter the team number of the AWAY team or enter "exit" to end the season: 1

Results of game 1 on 2024-11-05: Home team Utah State scored 2 - Away team BYU scored 0.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: 1
Enter the team number of the AWAY team or enter "exit" to end the season: 2

Results of game 2 on 2024-11-06: Home team BYU scored 0 - Away team UVU scored 2.

1: BYU
2: UVU
3: Utah State
Enter the team number of the HOME team or enter "exit" to end the season: exit

The soccer season is over!
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option: 2

Game Info Menu:
Game 1
Game 2
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: asdf
Invalid game number! Try again.


Game Info Menu:
Game 1
Game 2
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: 4
Invalid game number! Try again.


Game Info Menu:
Game 1
Game 2
Enter a game number to see its info, or enter "exit" to go back to the Postseason Menu: exit
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option: exit
Exiting the program.
```
