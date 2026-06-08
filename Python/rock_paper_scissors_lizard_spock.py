# rock paper scissors

import random

print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")
print("\n1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")


# 1) ask for player input and convert the players number to emoji
player = int(input("Pick a number: "))

if player == 1:
    player_emoji = '✊'
elif player == 2:
    player_emoji = '✋'
elif player == 3:
    player_emoji = '✌️'
elif player == 4:
    player_emoji = '🦎'
elif player == 5:
    player_emoji = '🖖'


# 2) create a computer choice and convert the computer number to emoji
computer = random.randint(1, 5)

if computer == 1:
    computer_emoji = '✊'
elif computer == 2:
    computer_emoji = '✋'
elif computer == 3:
    computer_emoji = '✌️'
elif computer == 4:
    computer_emoji = '🦎'
elif computer == 5:
    computer_emoji = '🖖'


# 3) create a control flow to compare with player and computer
if player == computer:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("Its a tie!")
elif player == 3 and computer == 2:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("The player won!")
elif player == 2 and computer == 1:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("The player won!")
elif player == 1 and computer == 4:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("The player won!")
elif player == 4 and computer == 5:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("The player won!")
elif player == 5 and computer == 3:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("The player won!")
elif player == 3 and computer == 4:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("The player won!")
elif player == 4 and computer == 2:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("The player won!")
elif player == 2 and computer == 5:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("The player won!")
elif player == 5 and computer == 1:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("The player won!")
elif player == 1 and computer == 3:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("The player won!")
else:
    print(f"\nYou chose: {player_emoji}")
    print(f"CPU chose: {computer_emoji}")
    print("The CPU won!")