#This game is sinmple Rock, Paper, Siccors
print("     Rock Paper Scissor Game     ")


print("[For Paper p]", "[for scissor : s]", " [For rock : r]")
 
import random

while True:
    player = input("YOU : ").lower()

    computer= random.choice(['r','s','p'])
    print('AI :', computer)
    if player =='s' and computer == 'p':
        print('YOU WON')
    elif player == 's'  and computer =='r':
        print("You Lost")

    elif player == 's' and computer =='s' :
        print('Draw')
    elif player == 'r' and computer == 's':
        print('You Won')
    elif player == 'r' and computer == 'p':
        print('You Lost')
    elif player == 'r' and computer == 'r':
        print('Draw')

    elif player == 'p'  and computer == 'r':
        print('You Won')
    elif player == 'p'  and computer == 's':
        print("You Lost")
    elif player == 'p'  and computer == 'p':
        print('Draw')
    else :
        print("Invalid Input, You are out of game")
        break
        
    repeat = input('To play again press x : ').lower()
    if repeat != 'x':
        break

