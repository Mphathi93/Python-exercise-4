# Question 1: Using a for loop with a list

# TODO: Create a list of fruits

# TODO: Use a for loop to print each fruit in the list
fruit = ["apple", "watermelon", "avocado", "kiwi", "Papaya"]
print("list of fruits")
for fruit in fruit:
    print(fruit)
 
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1

n = 5
while n >=1:
    print(n)
    n -=1
#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
print("The first 10 square numbers")
for number in range(1,11):
    square = number**2
    print(square)

#-------------------------------------------------------------------------

# #  Question 4: Using the random module

# #  TODO: Import the random module
import random
# #  TODO: Create a list of colors
 
#  TODO: Use a for loop to select and print 3 random colors from the list
colours = ["Crimson", "Sapphire", "Indigo", "Lavender", "Slate", "Cobalt", "Charcoal", "Burgundy", "Periwinkle", "Teal"]
for colour in range(0,3):
     c =  random.choice(colour)
print(c)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
# """
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error: Division by zero"
# """

# TODO: Import the custom module and use its functions
import math_op
# TODO: Use a while loop to create a simple calculator

def get_op():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    return input("Enter choice (1/2/3/4) or 'q' to quit: ")


while True:
    choice = get_op() 

    if choice == 'q':
        print("Exiting calculator.")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {math_op.add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {math_op.subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {math_op.multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {math_op.divide(num1, num2)}")

        except ValueError:
            print("Invalid input! Please enter numerical values.")
    else:
        print("Invalid choice! Please choose a valid operation.")