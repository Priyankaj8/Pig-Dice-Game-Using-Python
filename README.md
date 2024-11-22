# Pig Game

## Description
Pig is a simple dice game where players take turns rolling a die to earn points. The goal is to be the first player to reach the maximum score of 50 without rolling a 1, which ends the player's turn and resets their current turn score.

## How to Play
- The game supports 2 to 4 players.
- Players take turns rolling a die.
### On each roll:
- If the die shows any number other than 1, the rolled value is added to the player's current turn score.
- If the die shows 1, the player's turn ends, and their current turn score is reset to 0.
- At the end of each turn, the player can choose to:
  - Roll again to add to their turn score.
  - Stop and save their current turn score to their total score.
- The first player to reach a total score of 50 or more wins the game.

## Features
- **Randomized Dice Rolls:** Uses Python's random.randint to simulate dice rolls.
- **Player Management:** Supports 2 to 4 players.
- **Turn-Based Gameplay:** Players can decide whether to roll again or end their turn.
- **Dynamic Scoring:** Scores are tracked and displayed after each player's turn.

## Requirements
- Python 3.x
- No additional libraries are required as it uses Python's built-in random module.

## How to Run the Game
- Save the script to a file, e.g., pig_game.py.
- Open a terminal or command prompt.
- Run the game using the following command:
```bash
python main.py
```

## Example Gameplay
### Start
- **Prompt:** Enter the number of players (2 - 4).
   - Input the number of players (e.g., 3).
### During a Player's Turn
- **Prompt:** "Player number X turn has just started!"
   - The player can decide to roll or end their turn.
### Dice Rolls
- Rolling the dice displays the outcome:
  - If the result is 1: "You rolled a 1! Turn done!"
  -   Otherwise: "You rolled a: X" and the current score is updated.
- End of Turn
  - Displays the player's total score and moves to the next player.
- Winner Announcement
  - The game announces the winner:
```text
Player number X is the winner with a score of: Y
```
## Sample Output
```plaintext
Enter the number of players(2-4): 2

Player number 1 turn has just started!
Your total score is: 0 

Would you like to roll the dice?(y/n)y
Your rolled a:  4
Your score is: 4
Would you like to roll the dice?(y/n)y
You rolled a 1! Turn done!
Your total score is: 0

Player number 2 turn has just started!
Your total score is: 0 

Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 5
Would you like to roll the dice?(y/n)y
You rolled a 1! Turn done!
Your total score is: 0

Player number 1 turn has just started!
Your total score is: 0 

Would you like to roll the dice?(y/n)y
Your rolled a:  4
Your score is: 4
Would you like to roll the dice?(y/n)y
Your rolled a:  4
Your score is: 8
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 13
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 18
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 24
Would you like to roll the dice?(y/n)y
Your rolled a:  2
Your score is: 26
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 31
Would you like to roll the dice?(y/n)y
Your rolled a:  2
Your score is: 33
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 39
Would you like to roll the dice?(y/n)y
Your rolled a:  3
Your score is: 42
Would you like to roll the dice?(y/n)y
Your rolled a:  4
Your score is: 46
Would you like to roll the dice?(y/n)y
Your rolled a:  2
Your score is: 48
Would you like to roll the dice?(y/n)y
You rolled a 1! Turn done!
Your total score is: 0

Player number 2 turn has just started!
Your total score is: 0

Would you like to roll the dice?(y/n)y
Your rolled a:  3
Your score is: 3
Would you like to roll the dice?(y/n)y
You rolled a 1! Turn done!
Your total score is: 0

Player number 1 turn has just started!
Your total score is: 0

Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 6
Would you like to roll the dice?(y/n)y
Your rolled a:  4
Your score is: 10
Would you like to roll the dice?(y/n)y
Your rolled a:  4
Your score is: 14
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 19
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 24
Would you like to roll the dice?(y/n)y
Your rolled a:  4
Your score is: 28
Would you like to roll the dice?(y/n)y
Your rolled a:  2
Your score is: 30
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 35
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 41
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 46
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 51
Would you like to roll the dice?(y/n)y
You rolled a 1! Turn done!
Your total score is: 0

Player number 2 turn has just started!
Your total score is: 0

Would you like to roll the dice?(y/n)y
Your rolled a:  2
Your score is: 2
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 8
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 13
Would you like to roll the dice?(y/n)y
You rolled a 1! Turn done!
Your total score is: 0

Player number 1 turn has just started!
Your total score is: 0 

Would you like to roll the dice?(y/n)y
Your rolled a:  3
Your score is: 3
Would you like to roll the dice?(y/n)y
Your rolled a:  3
Your score is: 6
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 12
Would you like to roll the dice?(y/n)y
You rolled a 1! Turn done!
Your total score is: 0

Player number 2 turn has just started!
Your total score is: 0

Would you like to roll the dice?(y/n)y
Your rolled a:  4
Your score is: 4
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 10
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 15
Would you like to roll the dice?(y/n)y
Your rolled a:  3
Your score is: 18
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 24
Would you like to roll the dice?(y/n)y
Your rolled a:  4
Your score is: 28
Would you like to roll the dice?(y/n)y
Your rolled a:  4
Your score is: 32
Would you like to roll the dice?(y/n)n
Your total score is: 32

Player number 1 turn has just started!
Your total score is: 0

Would you like to roll the dice?(y/n)y
Your rolled a:  2
Your score is: 2
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 8
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 14
Would you like to roll the dice?(y/n)y
Your rolled a:  3
Your score is: 17
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 22
Would you like to roll the dice?(y/n)y
Your rolled a:  3
Your score is: 25
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 31
Would you like to roll the dice?(y/n)n
Your total score is: 31

Player number 2 turn has just started!
Your total score is: 32

Would you like to roll the dice?(y/n)y
You rolled a 1! Turn done!
Your total score is: 32

Player number 1 turn has just started!
Your total score is: 31

Would you like to roll the dice?(y/n)y
You rolled a 1! Turn done!
Your total score is: 31

Player number 2 turn has just started!
Your total score is: 32

Would you like to roll the dice?(y/n)
Your total score is: 32

Player number 1 turn has just started!
Your total score is: 31

Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 5
Would you like to roll the dice?(y/n)n
Your total score is: 36

Player number 2 turn has just started!
Your total score is: 32

Would you like to roll the dice?(y/n)y
Your rolled a:  2
Your score is: 2
Would you like to roll the dice?(y/n)y
You rolled a 1! Turn done!
Your total score is: 32

Player number 1 turn has just started!
Your total score is: 36

Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 5
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 11
Would you like to roll the dice?(y/n)y
Your rolled a:  6
Your score is: 17
Would you like to roll the dice?(y/n)n
Your total score is: 53

Player number 2 turn has just started!
Your total score is: 32

Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 5
Would you like to roll the dice?(y/n)y
Your rolled a:  3
Your score is: 8
Would you like to roll the dice?(y/n)y
Your rolled a:  5
Your score is: 13
Would you like to roll the dice?(y/n)y
Your rolled a:  3
Your score is: 16
Would you like to roll the dice?(y/n)y
Your rolled a:  4
Your score is: 20
Would you like to roll the dice?(y/n)n
Your total score is: 52
Player number 1 is the winner with a score of: 53
```
### Rules Recap
- Rolling 1 ends the turn and resets the current score.
- Players must strategize when to stop rolling and save their score.
