# Test Case 6

## Description
Invalid Postseason menu option

## Inputs
```
1: "3"
2: "BYU"
3: "N"
4: "UVU"
5: "N"
6: "Utah State"
7: "N"
8: "exit"
9: "asdf"
10: "exit"
```

## Expected Input Prompts
```
1: "Enter the number of soccer teams you want to enter (at least 2): "
2: "Enter a name for team 1: "
3: "Enter Y if team 1 is sponsored, otherwise enter N (or anything else): "
4: "Enter a name for team 2: "
5: "Enter Y if team 2 is sponsored, otherwise enter N (or anything else): "
6: "Enter a name for team 3: "
7: "Enter Y if team 3 is sponsored, otherwise enter N (or anything else): "
8: "Enter the team number of the HOME team or enter "exit" to end the season: "
9: "Enter an option: "
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
9: "Invalid choice! Try again."
10: "Exiting the program."
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
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
Enter the team number of the HOME team or enter "exit" to end the season: exit

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

Enter an option: exit
Exiting the program.
```
