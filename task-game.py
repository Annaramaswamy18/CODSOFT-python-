import random
fl=1
while fl==1:
    print("welcomr to Rock-Paper-Scissors game")
    print("Menu: \n Press 1 for Rock \n Press 2 for Paper \n Press 3 for Scissors")
    n=int(input("Enter the choice :"))
    h=random.randint(1,3)
    if(n==1 and h==2):
        print("Your choice is:",n,"   Computer choice is :",h,"   Result is :You've Lost")
    elif(n==1 and h==3):
        print("Your choice is:",n,"   Computer choice is :",h,"   Result is :You've won")
    elif(n==h):
        print("Your choice is:",n,"   Computer choice is :",h,"   Result is :Match Draw")
    elif(n==2 and h==3):
        print("Your choice is:",n,"   Computer choice is :",h,"   Result is :You've Lost")
    elif(n==2 and h==1):
        print("Your choice is:",n,"   Computer choice is :",h,"   Result is :You've won")
    elif(n==h):
        print("Your choice is:",n,"   Computer choice is :",h,"   Result is :Match Draw")
    elif(n==3 and h==1):
        print("Your choice is:",n,"   Computer choice is :",h,"   Result is :You've Lost")
    elif(n==3 and h==2):
        print("Your choice is:",n,"   Computer choice is :",h,"   Result is :You've won")
    elif(n==h):
        print("Your choice is:",n,"   Computer choice is :",h,"   Result is :Match Draw")
    choice=int(input("If you want to continue the game Press 1 else 0: "))
    if(choice==0):
        break
