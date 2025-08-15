### Snake-Water-Gun game:
'''
Values:
Snake = 1
Water = -1
Gun = 0
'''
import random

while True:
    computerchoice= random.choice([-1, 0, 1])    # for random choice
    computer=computerchoice
    computerdict= {1:'Snake', -1: 'Water', 0: 'Gun' }

    youinpt=input("Enter a key between 'S', 'W', 'G': ").lower()
    youdict = {'s': 1, 'w': -1, 'g': 0}

    if youinpt not in youdict:    # check for invalid input
        print("Invalid input!")
        exit()
    you = youdict[youinpt]

    # To understand what computer and user exactly took between s, w, g:
    computerYo= computerdict[computerchoice]
    youYo = computerdict[you]
    print(f"You choose: {youYo}\nComputer choose: {computerYo}")

    if(computer==you):
        print("Draw😐")
    else:
        if (computer==-1 and you==1): 
            print("You win 😎")
        elif (computer==-1 and you==0): 
            print("You loose 🤡")

        elif (computer==1 and you==-1):  
            print("You loose 🤡")
        elif (computer==1 and you==0): 
            print("You win 😎")

        elif (computer==0 and you==1): 
            print("You loose 🤡")
        elif (computer==0 and you==-1): 
            print("You win 😎")
