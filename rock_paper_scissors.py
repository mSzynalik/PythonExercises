"""
This program is a simple version of rock-paper-scissors game. Player faces computer random choices
and program tells who won and with what result game ended.
Author: Mateusz Szynalik
Date: 29.10.2021
"""
from random import randint  # Randint module imported to generate computer's choices.

players_points = 0
computers_points = 0
players_choice = ""
computers_choice = ""
choice = ""


def welcome():
    print(f"Hello Player! It's time to play!\nToday you will be facing computer in rock-paper-scissors game.\n"
          f"Please, follow given instructions and remember that computer's moves are chosen by pseudorandom numbers.\n"
          f"Please remember also that the game ends when you or computer will reach third point.\n"
          f"little test"
          f"Just to remind you - rock beats scissors, paper beats rock and scissors beats paper!")


def choice_reset():  # Player's choice needs to be changed to give player a possibility to choose a new one.
    global choice
    choice = ""
    return choice


def result():
    print(f"Game finished!")
    if players_points == 3:
        print(f"You won! The result of the game is:\nPlayer - {players_points}p.\nComputer - {computers_points}p.")
    elif computers_points == 3:
        print(f"You've been beaten by computer! The result of the game is:\n"
              f"Player - {players_points}p.\nComputer - {computers_points}p.")


welcome()
print()
while not (players_points == 3 or computers_points == 3): 
    while choice != 'p' and choice != 'r' and choice != 's':
        choice = input("Hey! What you want to choose? r - rock, p - paper, s - scissors: ")
    players_choice = choice
    computers_choice = randint(0, 2)
    if computers_choice == 0:
        computers_choice = 'r'
    elif computers_choice == 1:
        computers_choice = 'p'
    else:
        computers_choice = 's'
    if (players_choice == 'r' and computers_choice == 's') or (players_choice == 'p' and computers_choice == 'r') or (players_choice == 's' and computers_choice == 'p'):
        print(f"Point for you! Your choice - '{players_choice}', computer's choice - '{computers_choice}'.")
        players_points += 1
        choice_reset()
    elif players_choice == computers_choice:
        print(f"It's a draw in this round. You and computer both have chosen '{players_choice}'.")
        choice_reset()
    else:
        print(f"Point for the machine! Your choice - '{players_choice}', computer's choice - '{computers_choice}'.")
        computers_points += 1
        choice_reset()
print()
result()