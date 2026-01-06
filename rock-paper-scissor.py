'''
0 for rock
1 for paper
2 for scissors
'''

import random

computer = random.choice([0, 1, 2])

your_choice = input("enrte r for rock, p for paper, s for scissors: ")

youdict = {'r': 0, 'p': 1, 's': 2}
you = youdict[your_choice]

reversedict = {0: 'rock', 1: 'paper', 2: 'scissors'}



print(f"computer chose {reversedict[computer]}")
print(f"you chose {reversedict[you]}")

if ( you == computer):
    print("it's a tie")

else:
    if(you == 0 and computer == 1):
        print("computer wins")

     
    elif(you == 0 and computer == 2):
        print("you win")

    elif(you == 1 and computer == 0):
        print("you win")

    elif(you == 1 and computer == 2):
        print("computer wins")

    elif(you == 2 and computer == 0):
        print("computer wins")

    elif(you == 2 and computer == 1):
        print("you win")

    else:
        print("invalid input")
    
