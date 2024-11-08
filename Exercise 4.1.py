#------------------------------------------------------------------------------------
#Task 1: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.

# TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees ["Bob", "David"], and print the result.

# students = ["Alice", "Bob", "Charlie", "David"]
# absentees = ["Bob", "David"]

# def check_attendance(students, absentees):
#     return [student for student in students if student in absentees]

# absent_students = check_attendance(students, absentees)
# print("Absent students:", absent_students)

#------------------------------------------------------------------------------------
# Task 2: Function for Real-Life Data Processing

# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.

# TODO: Call the 'calculate_average_grade' function with the following dictionary:
#       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.
# calculate_average_grade = {
#     "Alice" : 85,
#     "Bob" : 92,
#     "Charlie" : 78,
#     "David" : 90
#     }
# avgrade = sum(calculate_average_grade.values())/ len(calculate_average_grade.values())
# print(avgrade)
#------------------------------------------------------------------------------------
# Task 3: Function Returning a Function (Higher-Order Function)

# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.

# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.

# TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.

#------------------------------------------------------------------------------------
# Task 4: Function for a Practical Scenario

# TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# • and returns the total cost of fuel for the trip.
# Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)

# TODO: Create a dictionary with grocery items as keys and their quantities in stock as values.
# grocery_inventory = {
#     "Apples": 50,
#     "Bananas": 30,
#     "Tomatoes": 25,
#     "Bread": 15,
#     "Milk": 10
# }

# TODO: Use a for loop to print each item and its quantity in stock.
# for item, quantity in grocery_inventory.items():
#     print(f"{item}: {quantity}")

# TODO: Calculate and print the total number of items in stock (sum of all values in the dictionary).

# total = sum(grocery_inventory.values())
# print(total)
# #------------------------------------------------------------------------------------
# # Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)

# # TODO: Ask the user to input their PIN.
# # TODO: If the PIN is incorrect, ask the user to try again, but only allow 3 attempts.
# # TODO: After 3 incorrect attempts, print "Account Locked". If the PIN is correct, print "Access Granted".

# correct_pin = "1234"
# attempts = 0
# max_attempts = 3

# while attempts < max_attempts:
    
#     user_input = input("Please enter your PIN: ")
    
#     if user_input == correct_pin:
#         print("Access Granted.")
#         break 
#     else:
#         print("Incorrect PIN. Please try again.")
#         attempts += 1 
# if attempts == max_attempts:
#     print("Account Locked.")

# TODO: Use a while loop to implement the retry system.

#------------------------------------------------------------------------------------
# Task 6: Using a for loop with range() for a School Grading System

# TODO: Create a list with 10 random assignment scores (between 0 and 100).
# TODO: Use a for loop to calculate the total score.
# TODO: Calculate and print the average score for the class.
# Bonus: Use conditional logic to print a congratulatory message if the average is above 75.

assignment = [50, 57, 72, 99, 69, 39, 17, 54, 8, 20]

import random

# List of 10 student scores.
scores = [random.randint(0, 100) for _ in range(10)]

# TODO: Calculate total and average scores.


#------------------------------------------------------------------------------------
# Task 7: Using the random module (Real-life Scenario: Random Team Selection)

# TODO: Create a list with the names of 20 participants.
# TODO: Use the random module to select 5 random participants.  
# TODO: Print the names of the selected team members.

import random

# List of participants.
# participants = ["Person1", "Person2", "Person3", ..., "Person20"]

# TODO: Randomly select 5 people from the participants list.


#------------------------------------------------------------------------------------
# Task 8: Custom module for a Fitness Tracker (Real-life Scenario: Tracking Calories Burned)

# Step 1: Create a module named 'fitness_tracker.py' with the following functions:
"""
def walk_calories(distance_km):
    # Calories burned per km walking: 50
    return distance_km * 50

def run_calories(distance_km):
    # Calories burned per km running: 100
    return distance_km * 100

def cycle_calories(distance_km):
    # Calories burned per km cycling: 70
    return distance_km * 70
"""

# Step 9: Use the custom module in your main script:
# TODO: Import the custom 'fitness_tracker' module.
# TODO: Ask the user to input the distance they walked, ran, and cycled today.
# TODO: Calculate and print the total calories burned for each activity.
# TODO: Sum and print the total calories burned for the day.


#------------------------------------------------------------------------------------
# Task 10: Using a while loop to Simulate Loan Repayment (Real-life Scenario: Paying Off a Loan)

# TODO: Ask the user to input the total loan amount.
# TODO: Ask the user to input their monthly repayment amount.
# TODO: Use a while loop to simulate monthly payments, reducing the loan each month.
# TODO: Print the remaining loan amount after each payment.
# TODO: When the loan is fully paid off, print a congratulatory message.

# loan_amount = float(input("Enter the total loan amount: "))
# monthly_payment = float(input("Enter your monthly payment amount: "))

# TODO: Use a while loop to simulate the repayment process.

