# Test Case 3

## Description
3 teams, 1 sponsored team, but no games played to test handling of potential zero division error

## Inputs
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

## Expected Input Prompts
```
1: "Enter the number of soccer teams you want to enter (at least 2): "
2: "Enter a name for team 1: "
3: "Enter Y if team 1 is sponsored, otherwise enter N (or anything else): "
4: "Enter the name of your sponsor: "
5: "Enter a name for team 2: "
6: "Enter Y if team 2 is sponsored, otherwise enter N (or anything else): "
7: "Enter a name for team 3: "
8: "Enter Y if team 3 is sponsored, otherwise enter N (or anything else): "
9: "Enter the team number of the HOME team or enter "exit" to end the season: "
10: "Enter an option: "
11: "Enter a team number to see their info, or enter "exit" to go back to the Postseason Menu: "
```

## Expected Printed Messages
```
1: "1: BYU"
2: "2: UVU"
3: "3: Utah State"
4: "The soccer season is over!"
5: "Postseason Menu:"
6: "1: Go to Team Info Menu"
7: "2: Go to Game Info Menu"
8: "exit: End the program"
9: "Team Info Menu:"
10: "Team Name: BYUSeason record: 0 - 0 (0%)Total goals scored: 0 - Total goals allowed: 0"
11: "Your team needs to practice! You are in danger of Cosmo dropping you."
12: "Exiting the program."
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
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
