# game Snake Water Gun
import random
computer=0
user=0
number_of_rounds=0
while number_of_rounds<10:
    number_of_rounds+=1
    print(f"\nYou have 10 chance and you have used {number_of_rounds -1} chances")
    print(f"computer points:{computer} user points:{user}")
    choice=input("enter your choice snake,water,gun: ")
    # ------------if u need to enter one letter as input (s,w,g)------------------
    """
    if choice=="s":
        choice="snake"
    elif choice=="w":
        choice="water"
    elif choice=="g":
        choice="gun"
    else:
        print("invalid input")
    """
    #-----------------------------------------------------------------------
    items=["snake","water","gun"]
    Autogenerate=random.choice(items)
    print(f"you have choosen: {choice} and computer has choosen: {Autogenerate}")
    if choice=="snake" and Autogenerate=="snake":
        print("no one gets the point as the game is draw")
    elif choice == "snake" and Autogenerate == "water":
        user+=1
        print("user gets the point")
    elif choice == "snake" and Autogenerate == "gun":
        computer+=1
        print("computer gets the point")

    elif choice=="water"and Autogenerate =="snake":
        computer+1
        print("computer gets the point")
    elif choice == "water" and Autogenerate =="water":
        print("no one gets the point as the game is draw")
    elif choice == "water" and Autogenerate == "gun":
        user+=1
        print("user gets the point")

    elif choice=="gun"and Autogenerate =="snake":
        user+=1
        print("user gets the point")
    elif choice == "gun" and Autogenerate =="water":
        computer+=1
        print("computer gets the point")
    elif choice == "gun" and Autogenerate =="gun":
        print("no one gets the point as the game is draw")
    else:
        print("invalid input type full word or correct word and try again")

print("\ngame over you have compleated 10 rounds")
if computer > user:
    print(f"computer won the game and scores are computer:{computer} user:{user}")
elif computer==user:
    print(f"the scores are computer:{computer} and user:{user} the game is draw play again")
else:
    print(f"user won the game and scores are computer:{computer} user:{user}")