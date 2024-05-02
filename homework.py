#======= Question 1 =======

# Task 1 : Write functions for addition, subtraction, multiplication, and division

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

# Task 2 : Get numbers and operation

num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")
operation = input("Would you like to add, subtract, multiply, or divide: ")

# Task 3 : Safely perform operation

safe = True

if num_1.isdigit():
    num_1 = int(num_1)
elif num_1.replace(".","").isdigit():
    num_1 = float(num_1)
else:
    print("First number is unreadable")
    safe = False

if num_2.isdigit():
    num_2 = int(num_2)
elif num_2.replace(".","").isdigit():
    num_2 = float(num_2)
else:
    print("Second number is unreadable")
    safe = False

if operation not in ["add","subtract","multiply","divide"]:
    print("Operation is unreadable")
    safe = False

if safe:
    if operation == "add":
        print(f"{num_1} + {num_2} = {add(num_1, num_2)}")
    elif operation == "subtract":
        print(f"{num_1} - {num_2} = {subtract(num_1, num_2)}")
    elif operation == "multiply":
        print(f"{num_1} * {num_2} = {multiply(num_1, num_2)}")
    elif num_2 != 0:
        print(f"{num_1} / {num_2} = {divide(num_1, num_2)}")
    else:
        print("Unable to divide by zero.")
        safe = False


#======= Question 2 =======

# Task 1 : Building a shopping list

shopping_list = []

while True:
    item = input("Add item (-[item] to remove, quit to quit): ")
    item = item.strip()
    if item == "quit":
        break
    # Task 2 : Item removal
    elif item[0] == "-":
        item = item[1:].strip()
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print(f"No {item} in shopping list.")
    else:
        shopping_list.append(item)

# Task 3 : Print contents of shopping cart

if len(shopping_list) == 0:
    print("Your shopping list is empty.")
elif len(shopping_list) == 1:
    print(f"Your shopping list contains only {shopping_list[0]}.")
elif len(shopping_list) == 2:
    print(f"Your shopping list contains {shopping_list[0]} and {shopping_list[1]}.")
else:
    print("Your shopping list contains ", end = "")
    for item in shopping_list[:-1]:
        print(item + ", ", end = "")
    print(f"and {shopping_list[-1]}.")