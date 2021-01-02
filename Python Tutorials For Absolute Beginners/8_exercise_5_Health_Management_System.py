#  Health Management System
def datetime():
    import datetime
    return datetime.datetime.now()
# functions to write data in the file
def lock(choice):
    if choice == 1:
        choice1 = int(input("1)diet 2)exercise: "))
        if choice1 == 1:
            value1 = input("enter the value to append to the Harry file: ")
            with open("Harry_diet.txt", "a") as file1:
                file1.write("[" + str(datetime()) + "]:" + value1 + "\n")
            print("successfully written""\n", datetime(), value1)
        elif choice1 == 2:
            value1 = input("enter the value to append to the Harry file: ")
            with open("Harry_exercise.txt", "a") as file2:
                file2.write("[" + str(datetime()) + "]:" + value1 + "\n")
            print("successfully written""\n", datetime(), value1)
        else:
            print("Invalid input")
    elif choice == 2:
        choice2 = int(input("1)diet 2)exercise: "))
        if choice2 == 1:
            value2 = input("enter the value to append to the Rohan file: ")
            with open("Rohan_diet.txt", "a") as file3:
                file3.write("[" + str(datetime()) + "]:" + value2 + "\n")
            print("successfully written""\n", datetime(), value2)
        elif choice2 == 2:
            value2 = input("enter the value to append to the Rohan file: ")
            with open("Rohan_exercise.txt", "a") as file4:
                file4.write("[" + str(datetime()) + "]:" + value2 + "\n")
            print("successfully written""\n", datetime(), value2)
        else:
            print("Invalid input")
    elif choice == 3:
        choice3 = int(input("1)diet 2)exercise: "))
        if choice3 == 1:
            value3 = input("enter the value to append to the Hammad file: ")
            with open("Hammad_diet.txt", "a") as file5:
                file5.write("[" + str(datetime()) + "]:" + value3 + "\n")
            print("successfully written""\n", datetime(), value3)
        elif choice3 == 2:
            value3 = input("enter the value to append to the Hammad file: ")
            with open("Hammad_exercise.txt", "a") as file6:
                file6.write("[" + str(datetime()) + "]:" + value3 + "\n")
            print("successfully written""\n", datetime(), value3)
        else:
            print("Invalid input")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
# functions to read the contents in the file
def Retrieve(select):
    if select == 1:
        select1 = int(input("1)diet 2)exercise: "))
        if select1 == 1:
            with open("Harry_diet.txt") as file1:
                for line in file1:
                    print(line, end="")
        elif select1 == 2:
            with open("Harry_exercise.txt") as file1:
                for line in file1:
                    print(line, end="")
        else:
            print("Invalid input")
    elif select == 2:
        select2 = int(input("1)diet 2)exercise: "))
        if select2 == 1:
            with open("Rohan_diet.txt") as file1:
                for line in file1:
                    print(line, end="")
        elif select2 == 2:
            with open("Rohan_exercise.txt") as file1:
                for line in file1:
                    print(line, end="")
        else:
            print("Invalid input")
    elif select == 3:
        select3 = int(input("1)diet 2)exercise: "))
        if select3 == 1:
            with open("Hammad_diet.txt") as file1:
                for line in file1:
                    print(line, end="")
        elif select3 == 2:
            with open("Hammad_exercise.txt") as file1:
                for line in file1:
                    print(line, end="")
        else:
            print("Invalid input")
    else:
        print("plz enter valid input (harry,rohan,hammad)")
# To choose the option of write or display the content
selection = int(input("Health Management\n1)lock value 2)Retrieve value: "))
if selection == 1:
    choice = int(input("1)Harry 2)Rohan 3)Hammad: "))
    lock(choice)
elif selection == 2:
    select = int(input("1)Harry 2)Rohan 3)Hammad: "))
    Retrieve(select)
else:
    print("Invalid input")

####################################################################################
"""
# Problem methot2 using dictionary
client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
lock_list = {1: "Exercise", 2: "Diet"}


def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())

    print("Selected Client : ", client_list[client_name], "\n", end="")

    print("Press 1 for Lock")
    print("Press 2 for Retrieve")
    op = int(input())

    if op is 1:
        for key, value in lock_list.items():
            print("Press", key, "to lock", value, "\n", end="")
        lock_name = int(input())
        print("Selected Job : ", lock_list[lock_name])
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
        k = 'y'
        while (k is not "n"):
            print("Enter", lock_list[lock_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()
    elif op is 2:
        for key, value in lock_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        lock_name = int(input())
        print(client_list[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")
"""