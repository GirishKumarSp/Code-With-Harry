# Pattern printing
# program using while loop
number1 = int(input("enter number of rows: ")) #inserting the number of stars
print("0 for decending & 1 for ascending")
boolean_value = bool(int(input("enter method: "))) #inserting the type of pattren
if boolean_value==True: #converting the input to boolean value
   number2 = 0
   while number2 <= number1:
      print(number2 * "*")
      number2 += 1
elif boolean_value==False: #converting the input to boolean value
   while number1 >= 0:
      print(number1 * "*")
      number1 -= 1

#program using for loop
"""
rows=int(input("enter number of rows: "))
print("0 for decending & 1 for ascending")
choose=bool(int(input("enter method: ")))
if choose==1:
  for i in range (rows+1):
    print("*" * i)
else:
     for i in range (rows):
         choose= rows - i
         print("*" * choose)
"""




