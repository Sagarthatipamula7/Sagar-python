from random import *
def selecting_choice(user_choice,com_choice):
    if user_choice == com_choice:
        return "game is tie"
    elif (user_choice == "rock" and com_choice=="scissor" or 
          user_choice=="paper" and com_choice=="rock" or
          user_choice=="scissor" and com_choice=="paper"):
        return "user won the game"
    else:
        return "com won the game"
def game():
    choices=["rock","paper","scissor"]
    user_choice=input("enter any choice(rock/paper/scissor)")
    com_choice=choice(choices)
    output=selecting_choice(user_choice,com_choice)
    return output
print(game())

