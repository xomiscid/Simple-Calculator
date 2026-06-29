# ██╗  ██╗ ██████╗ ███╗   ███╗██╗███████╗ ██████╗██╗██████╗
# ╚██╗██╔╝██╔═══██╗████╗ ████║██║██╔════╝██╔════╝██║██╔══██╗
#  ╚███╔╝ ██║   ██║██╔████╔██║██║███████╗██║     ██║██║  ██║
#  ██╔██╗ ██║   ██║██║╚██╔╝██║██║╚════██║██║     ██║██║  ██║
# ██╔╝ ██╗╚██████╔╝██║ ╚═╝ ██║██║███████║╚██████╗██║██████╔╝
# ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝╚═════╝
#
#              Crafted by XOMISCID

#Fourth python project
#An simple calculator 

print("== WELCOME TO THE SIMPLE CALCULATOR :) ==")
print()
#Ask the user to choose their first number within a loop to handle the case where the user enters something other than a number
while True:
    try:
        num1 = float(input("Enter your first number :"))
        print()
        break
    #If the user enters anything other than a number, an error message appears, and since it is inside a loop, they are asked to re-enter the number
    except ValueError:
        print("You can only choose a number as your first number !")
        
#Ask the user to choose their second number within a loop to handle the case where the user enters something other than a number
while True:
    try:
        num2 = float(input("Enter your second number :"))
        print()
        break
    #If the user enters anything other than a number, an error message appears, and since it is inside a loop, they are asked to re-enter the number
    except ValueError:
        print("You can only choose a number as your second number !")

#Ask the user to choose an operator
operator = input("Choose an operator (+,-,/,*) :")
print()
#If the user enters anything other than the four operators (+, -, /, *), an error message appears, and they must re-enter the operator
while operator != '+' and operator != '-' and operator != '*' and operator != '/':
    operator = input("ERROR : choose one of this operators (+,-,/,*) :")
if operator == '+':
    #Create a result variable to store the result of the operation
    result = num1 + num2
    #Since the 'float' type was used to store the numbers, if the result and the input numbers are integers, we will display them as integers for aesthetic reasons
    if result.is_integer() and num1.is_integer() and num2.is_integer():
        num1 = int(num1)
        num2 = int(num2)
        result = int(result)
        print(f"{num1} + {num2} = {result}")
    #If the result and the numbers are not integers, the display will appear normally
    else:
        print(num1, " + ", num2, " = ",result)
elif operator == '-':
    #Create a result variable to store the result of the operation
    result = num1 - num2
 #Since the 'float' type was used to store the numbers, if the result and the input numbers are integers, we will display them as integers for aesthetic reasons
    if result.is_integer() and num1.is_integer() and num2.is_integer():
        num1 = int(num1)
        num2 = int(num2)
        result = int(result)
        print(f"{num1} - {num2} = {result}")
    #If the result and the numbers are not integers, the display will appear normally
    else:
        print(result)
elif operator == '*':
    #Create a result variable to store the result of the operation
    result = (num1 * num2)
 #Since the 'float' type was used to store the numbers, if the result and the input numbers are integers, we will display them as integers for aesthetic reasons
    if result.is_integer() and num1.is_integer() and num2.is_integer():
        num1 = int(num1)
        num2 = int(num2)
        result = int(result)
        print(f"{num1} * {num2} = {result}")
    #If the result and the numbers are not integers, the display will appear normally
    else: 
        print(result)
elif operator == '/':
    #For division, the code checks whether the second number is zero, since a number cannot be divided by zero; if it is not zero, the result is displayed, otherwise the code stops
    if num2 != 0:
    #Create a result variable to store the result of the operation
      result = num1 / num2
 #Since the 'float' type was used to store the numbers, if the result and the input numbers are integers, we will display them as integers for aesthetic reasons
      if result.is_integer() and num1.is_integer() and num2.is_integer():
        num1 = int(num1)
        num2 = int(num2)
        result = int(result)
        print(f"{num1} / {num2} = {result}")
    #If the result and the numbers are not integers, the display will appear normally
      else:
        print(result)
    #Display an error and stop execution if the second number in the division is zero
    else:
        print("ERROR : you can't divise a number by zero !")
print()
print("== THANK YOU :) ==")
