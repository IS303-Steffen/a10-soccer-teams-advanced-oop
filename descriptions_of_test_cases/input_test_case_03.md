# Test Case 3

## Description
3 teams, 1 sponsored team, but no games played to test handling of potential zero division error

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
9: "exit"
10: "1"
11: "1"
12: "exit"
13: "exit"
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
Season record: 0 - 0 (0%)
Total goals scored: 0 - Total goals allowed: 0

Your team needs to practice! You are in danger of Cosmo dropping you.


Team Info Menu:
1: BYU
2: UVU
3: Utah State
Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu: exit
Postseason Menu:
1: Go to Team Info Menu
2: Go to Game Info Menu
exit: End the program

Enter an option: exit
Exiting the program.
```
