# Test Case 4

## Description
Invalid integer and values less than 2 for the number of teams to create

## Inputs
```
1: "asdf"
2: "1"
3: "3"
4: "BYU"
5: "N"
6: "UVU"
7: "N"
8: "Utah State"
9: "N"
10: "exit"
11: "exit"
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
1: "Invalid integer! Try again."
2: "You must enter an integer of 2 or above. Try again."
3: "1: BYU"
4: "2: UVU"
5: "3: Utah State"
6: "The soccer season is over!"
7: "Postseason Menu:"
8: "1: Go to Team Info Menu"
9: "2: Go to Game Info Menu"
10: "exit: End the program"
11: "Exiting the program."
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
```
Enter the number of soccer teams you want to enter (at least 2): asdf
Invalid integer! Try again.

Enter the number of soccer teams you want to enter (at least 2): 1
You must enter an integer of 2 or above. Try again.

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

Enter an option: exit
Exiting the program.
```
