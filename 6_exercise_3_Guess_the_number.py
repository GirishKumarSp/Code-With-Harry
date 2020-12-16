number=18
count=0
fixed_guess=9
while(True):
    guess=int(input("Enter the guessing number: "))
    count+=1
    if guess==18:
        print("you have perfectly guessed the number")
        print("you have taken",count,"trys to complete")
        print("you had",fixed_guess-count,"trys left")
        break
    elif count==fixed_guess:
        print("you have exeded number of trys")
        print("you have",fixed_guess-count,"trys left")
        print("GAME OVER")
        break
    elif guess<18:
        print("This is wrong guess","Add some value to your guess")
        print("you have", fixed_guess - count, "trys left")
        continue
    elif guess>18:
        print("This is wrong guess","Reduce some value to your guess")
        print("you have", fixed_guess - count, "trys left")
        continue
