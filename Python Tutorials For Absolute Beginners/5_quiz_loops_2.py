while(True):
    num = int(input("enter the number to evaluate: "))
    if num < 100:
        print("Try again")
        continue
    if num > 100:
        print("yee you have entered more than 100")
        break

