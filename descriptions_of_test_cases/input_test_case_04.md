# Test Case 4

## Description
Invalid integer and values less than 2 for the number of teams to create

## Inputs
The inputs below (without the quotes) will be entered one by one each time an `input()` function is found in your code.
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

## Example Output
This is what your terminal should look like if you use the inputs above when running your code.
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
