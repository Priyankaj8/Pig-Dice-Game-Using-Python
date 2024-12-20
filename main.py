import random
def roll():
    roll =  random.randint(1,6)
    return roll
while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid, please enter a number")

max_score = 50
player_scores = [0 for _ in range(players)] # List comprehension
while max(player_scores)<max_score:

    for player_idx in range(players):
        print(f"\nPlayer number {player_idx+1} turn has just started!")
        print("Your total score is:",player_scores[player_idx],"\n")
        current_score = 0

        while True:
            choice = input("Would you like to roll the dice?(y/n)").lower()
            if choice != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("Your rolled a: ",value)

            print("Your score is:",current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:",player_scores[player_idx])
            
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player number {winning_idx+1} is the winner with a score of: {max_score}")