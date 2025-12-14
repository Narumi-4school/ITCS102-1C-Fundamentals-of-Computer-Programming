# Welcome to my Python Functions Compiler Program
import os
import time
import io
import sys

def type_writer(text, speed=0.016):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()

def conditional_stat(val):
    age = val
    if age >= 18:
        print("You are an adult")
    else:
        print("You are still a minor")

def Fl_Triangle(rows):
    for i in range(1, rows + 1):
        for space in range(rows - i):
            print(" ", end="")
        for star in range(2 * i - 1):
            print("*", end="")
        print()

code_triangle = """def Fl_Triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
"""

def clear_sc(any_key):
    any_key = input("Press any key to exit... ")
    os.system('cls')

def try_print():
    print("\nLet's practice the print() function!")
    print("Type the text you want to print (without quotes).")
    user_input = input("Your value: ")
    print("\nHere's what your print() would show:")
    print(user_input)

def show_menu():
    print("+------------------------------------+")
    print("WELCOME TO My PYTHON COMPILER SYSTEM")
    print("+------------------------------------+")
    name = input("What is your name? .....  ")
    print("Hello", name, "Choose an action from 1 - 9 --> ")
    print("1. Print function")
    print("2. View python sequences")
    print("3. Arithmetic assignations and functions")
    print("4. Logic operators")
    print("5. Conditional Statements")
    print("6. Loops")
    print("7. While Loops")
    print("8. Lists and Dictionaries")
    print("9. Python Fundamentals")
    print("X. Exit System")
    print("+------------------------------------+")

show_menu()

# Main Loop
while True:
    choice = input("Enter choice --> ")

    if choice == '1':
        type_writer("PRINTING FUNCTION IN PYTHON")
        print("+------------------------------------+")
        type_writer("We all started on Hello World on our Python journey.")
        type_writer("Choose an action below:")
        print("1. Print different data types")
        print("2. Try Print Function")
        print("3. Exit")
        user_choice = input("Enter choice: ")
        if user_choice == '1':
            type_writer("Data types in Python.")
            print("+------------------------------------+")
            print("Str (String) used for printing text.\n")
            print("Int (Integer) used for whole numbers.\n")              
            print("Float is used for numbers with decimals.\n")
            print("Bool (Boolean) has only 2 values (True) or (False).\n")
            print("List is used for listing values in one variable.\n")
            print("Dict (Dictionary) used for storing data with names.\n")
            print("None (result = None) represents empty / no value.")
            print("TIP: \nEval is used to automatically detect what type of data is being input")
            clear_sc('any_key')
            show_menu()
            continue
        elif user_choice == '2':
            print("TRY USING PRINT FUNCTION.")
            print("+------------------------------------+")
            try_print()
            clear_sc('any_key')
            show_menu()
        elif user_choice == '3':
            clear_sc('any_key')
            show_menu()
            continue

    elif choice == '2':
        type_writer("DIFFERENT PYTHON SEQUENCES IN PYTHON")
        print("Escape Sequence \t\t|\t\tDefinition \t\t|\t\tExample \t\t| \t\tOutput")
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        print("\\n \t\t\t\t\tNew Line \t\t\t\tprint('\\nHellowWorld') \t\t\tA\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tB")
        print("\\t \t\t\t\t\tTab space(indent) \t\t\tprint('Hello\\tWorld') \t\t\tHello\tWorld")
        print("\\ \t\t\t\t\tBackSlash \t\t\t\tprint('This is a back slash \\\')   This is a backslash \\")
        print("\\' \t\t\t\t\tSingle Quote \t\t\t\tprint('It\\'s Python') \t\t\tIt's Python")
        print("\\\" \t\t\t\t\tDouble Quote \t\t\t\tprint(\"I said \\\"Hi\\\"\") \t\t\tprint(\"I said \"Hi\"\")")
        print("\\r \t\t\t\t\tCarriage return(start of line) \t\tprint('Hello\\rWorld') \t\t\tWorld")
        print("\\b \t\t\t\t\tBack Space \t\t\t\tprint('Hello\\bWorld') \t\t\tHellWorld")
        print("\nKEY POINTS:")
        print("\\n - prints into a new line")
        print("\\t - inserts a tab space")
        print("\\ - used inside strings to give special meaning to characters that follows it")
        print("\\' - used to emphasize the single quote")
        print("\\\" - used to emphasize te double quote")
        print("\\r - returns the string into the start of the line")
        print("\\b - deletes the first string that follows it")
        clear_sc('any_key')
        show_menu()
        continue

    elif choice == '3':
        print("ARITHMETIC OPERATORS AND FUNCTIONS")
        print("Operator \t\t|\t\tSign \t\t|\t\tExample \t\t| \t\tOutput")
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("Addition \t\t\t\t+ \t\t\t\t5 + 3 \t\t\t\t\t8")
        print("Subtraction \t\t\t\t- \t\t\t\t5 - 3 \t\t\t\t\t2")
        print("Multiplication \t\t\t\t* \t\t\t\t5 * 3 \t\t\t\t\t15")
        print("Division \t\t\t\t+ \t\t\t\t10 / 2 \t\t\t\t\t5")
        print("Floor Division \t\t\t\t// \t\t\t\t5 // 2 \t\t\t\t\t2(drops decimal")
        print("Modulus \t\t\t\t% \t\t\t\t5 % 2 \t\t\t\t\t1(only gets the remainder)")
        print("Exponent \t\t\t\t+ \t\t\t\t5 ** 2 \t\t\t\t\t25(5 squared)")
        print("\nKEY POINT:")
        print("You can use the += for incrementation to improve code effiency by adding a value to a variable and updates it at the same time!")
        print("Example:")
        print("x = 5 \n\nx += 5 # adds and updates the variable \n\nprint(x) \n\n10")
        clear_sc('any_key')
        show_menu()
        continue
    elif choice == '4':
        print("+---------------------------------------------------------------------------------------------------------------------+")
        print("LOGIC OPERATORS")
        print("Operator \t|\tKeyword \t|\tMeaning \t| \tExample \t|\tOutput")
        print("+---------------------------------------------------------------------------------------------------------------------+")
        print("AND \t\t\tand \t\tTrue if both are True \t\tTrue and False \t\tFalse")
        print("OR \t\t\tor \t\tTrue if atleast one is True \tTrue or False \t\tTrue")
        print("NOT \t\t\tnot \t\tReverses the boolean value \tnot True \t\tFalse")
        type_writer("\nFurther Examples:")
        type_writer("AND \nx = 5 \ny = 10 \n print('x > 0 and y < 5') # True because both conditions are True")
        type_writer("print('x > 0 and y < 5) # False because y < 5 is False")
        type_writer("\nOR \nx = 5 \ny = 10 \nprint('x > 0 or y < 5) # True because x > 0 is True")
        type_writer("print('x < 0 or y < 5') # False because both conditions are false")
        type_writer("\nNOT \nx = True \ny = False \nprint('not x') # False, reverse of True \nprint('not y') \# True, reverse of False")
        clear_sc('any_key')
        show_menu()
        continue
    elif choice == '5':
        print("+---------------------------")
        print("CONDITIONAL STATEMENTS")
        print("+---------------------------")
        print("Explore different functions:")
        print("1. Explain conditional statements ")
        print("2. Try using conditional statements")
        print("3. Exit")
        user_choice1 = input("Input choice --> ")
        if user_choice1 == '1':
            type_writer("Let\'s start with the basics. Which is the if else statements.")
            time.sleep(1.3)
            type_writer("\n\t if condition: \n\t\t # executes the code if the condition is True")
            type_writer("\nExample: ")
            type_writer("number = 20 \nif number >= 20: \n\tprint('This number is greater than or equal 20)")
            type_writer("Ouput: \nThis number is greater than or equal 20")
            time.sleep(0.8)
            type_writer("Now let\'s proceed in If - Else statements")
            type_writer("\n if condition: \n\t# Execute code when True \n else condition: \n\t# Execute code when False")
            type_writer("Example:")
            type_writer("\n age = 13 \n if age >= 18:\n\tprint('You are an adult')\n else:\n\tprint('You are a minor')")
            clear_sc('any_key')
            show_menu()
            continue
        elif user_choice1 == '2':
            print("+---------------------------")
            choose = eval(input("Enter your age --> "))

            conditional_stat(choose)
            a = input("Do you want to see the code behind that? (y/n) ").lower()
            if a == 'y':
                print("def conditional_stat(val):\n\tage = val # gets the value from the def function \nif age >= 18: #checks if age is greater than or equal to 18 \n\tprint('You are an adult') # Prints if True \nelse: \n\tprint('You are still a minor') # Prints if false")
                continue
        elif user_choice1 == '3':
            print("You are directed to the main menu..")
            clear_sc('any_key')
            show_menu()
            continue
        else:
            
            print("Okay! Thank you for using this system.")
            clear_sc('any_key')
            show_menu()    
            continue

    elif choice == '6':
        print("+---------------------------")
        print("FOR LOOPS")
        print("+---------------------------")
        type_writer(f"\nNice progress! You are now on for loops")
        print("Choose from below:")
        print("1. Learn about for loops")
        print("2. Practice for loops")
        print("3. Exit")

        user_choice2 = input("Enter choice --> ")

        if user_choice2 == '1':
            type_writer("FOR LOOPS")
            type_writer("\nFor loops consists of many parts but let's start on the basics..")
            type_writer("First you need to create a structure")
            type_writer("Example: \nfor variable in  sequence(start, stop, step/s) # Basic structure of a for loop")
            type_writer("Let's take this one as an example: \n for i in range(1, 5, 1): \n\tprint(i) # Prints the number of sequence")
            type_writer("Output:\n1\n2\n3\n4")
            type_writer("\nLooping through a list:")
            type_writer("\n fruits = ['apple','banana','mango']")
            type_writer("\n for fruit in fruits: \n\tprint(fruit) # Iterates the list through a  loop")
            type_writer("\nOuput:")
            
            fruits = ["apple","banana","mango"]
            
            for fruit in fruits:
                print(fruit)
            type_writer("\nLooping using arithmetic")
            type_writer("\n Let's take this as an example.")
            type_writer("\n number = 0 # Create a empty variable for incrementation")
            type_writer("\n for i in range(1,6): \n\tnumber += i # Increment")
            type_writer("\nOutput:")
            
            number = 0
            for i in range(1,6):
                number += i
                print(number)
            # Using end="" to loop in the same line
            type_writer("\nPrinting list on the same line/horizontally")
            type_writer("\nBy using this keyword ('end=""'), it prints the loop in the same line")
            type_writer("\nExample:")
            type_writer("\n for i in range(1,6): \n\tprint(i,end=\" \")# Input space inside the keyword to add space each item")
            type_writer("\nprint() # To start a new line instead of the cursor appearing at the end of loop")
            type_writer(" print() # Add to the end of loop to start a new line")
            type_writer("\nOutput:")
            print()
            for i in range(1,6):
                print(i,end=" ")
            print()
            
            type_writer("\nLooping with if statement:")
            type_writer("\nYou can use other functions on for loops such as the previous ones and also conditional statements...")
            type_writer("\nfor i in range(1,11): \n\tif i % 2 == 0: \n\tprint(i,'is even')")
            type_writer("\nOutput:")
            print()
            for i in range(1, 11):
                if i % 2 == 0:
                   print(i, "is even")
            type_writer("\nNote that every basic function in python is fundamental in learning the whole language...")
            clear_sc('any_key')
            show_menu()
            continue
        elif user_choice2 == '2':
            type_writer("\nExplore different for loops.")
            type_writer("\n Choose from the choices below:")
            print("+----------------------------------------+")
            print("1. Triangle * for loop")
            print("2. List Iteration")
            print("3. For Loop with math")
            print("4. Exit")
            print()
            user_choice3 = input("Enter choice --> ")

            if user_choice3 == '1':
                print("Triangle * using for loop")
                print("+----------------------------------------+")
                row = eval(input("Enter desired number of rows --> "))
                Fl_Triangle(row)
                pr = input("Press enter to see the code... ")
                print(code_triangle)
                print()
                ex = input("Do you want to continue using the system? --> (y/n) ").lower()
                if ex == 'y':
                    clear_sc('any_key')
                    show_menu()
                    continue
                    

            elif user_choice3 == '2':
                print("List iteration")
                print("+----------------------------------------+")
                e_list = []
                print("Enter items to add to list. Type DONE when finished entering: ")

                while True:
                    item = input("Enter item: ")
                    if item.lower() == 'done':
                        break
                    e_list.append(item)
                print("Your list is:", e_list)
                pr = input("Press enter to iterate the list....")
                for items in e_list:
                    print(items)
                lh44 = input("Press enter again to see the code")
                code_list = """e_list = []
print("Enter items to add to list. Type DONE when finished entering: ")

while True:
    item = input("Enter item: ")
    if item.lower() == 'done':
        break
    e_list.append(item)
print("Your list is:",e_list)
for items in e_list:
    print(items)
"""
                print(code_list)
                ex = input("Do you want to continue to other loops?--> (y/n)").lower()
                if ex == 'y':
                    continue
        

            elif user_choice3 == '3':
                # Merged Arithmetic For Loops with code display
                print("FOR LOOP WITH ARITHMETIC OPERATORS")
                print("+----------------------------------------+")

                while True:
                    print("\nChoose an arithmetic operation to see in a for loop:")
                    print("1. Addition (+)")
                    print("2. Subtraction (-)")
                    print("3. Multiplication (*)")
                    print("4. Division (/)")
                    print("5. Exit to previous menu")

                    op_choice = input("Enter choice --> ")

                    if op_choice == '1':
                        code_add = """total = 0
for i in range(1, 6):
    total += i
    print(f"Adding {i}, total so far: {total}")
print(f"Final sum: {total}")"""
                        print("\nAddition in a for loop:")
                        total = 0
                        for i in range(1, 6):
                            total += i
                            print(f"Adding {i}, total so far: {total}")
                        print(f"Final sum: {total}")
                        input("\nPress any key to see the code behind Addition...")
                        print("\nCode behind Addition:\n")
                        print(code_add)

                    elif op_choice == '2':
                        code_sub = """result = 20
for i in range(1, 6):
    result -= i
    print(f"Subtracting {i}, result so far: {result}")
print(f"Final result: {result}")"""
                        print("\nSubtraction in a for loop:")
                        result = 20
                        for i in range(1, 6):
                            result -= i
                            print(f"Subtracting {i}, result so far: {result}")
                        print(f"Final result: {result}")
                        input("\nPress any key to see the code behind Subtraction...")
                        print("\nCode behind Subtraction:\n")
                        print(code_sub)

                    elif op_choice == '3':
                        code_mul = """product = 1
for i in range(1, 6):
    product *= i
    print(f"Multiplying by {i}, product so far: {product}")
print(f"Final product: {product}")"""
                        print("\nMultiplication in a for loop:")
                        product = 1
                        for i in range(1, 6):
                            product *= i
                            print(f"Multiplying by {i}, product so far: {product}")
                        print(f"Final product: {product}")
                        input("\nPress any key to see the code behind Multiplication...")
                        print("\nCode behind Multiplication:\n")
                        print(code_mul)

                    elif op_choice == '4':
                        code_div = """result = 120
for i in range(2, 6):
    result /= i
    print(f"Dividing by {i}, result so far: {result}")
print(f"Final result: {result}")"""
                        print("\nDivision in a for loop:")
                        result = 120
                        for i in range(2, 6):
                            result /= i
                            print(f"Dividing by {i}, result so far: {result}")
                        print(f"Final result: {result}")
                        input("\nPress any key to see the code behind Division...")
                        print("\nCode behind Division:\n")
                        print(code_div)

                    elif op_choice == '5':
                        clear_sc('any_key')
                        show_menu()
                        continue
                    else:
                        print("Invalid Choice.")
                        clear_sc('any_key')
                        show_menu()
                        continue
            elif user_choice3 == '4':
                print("You are directed to the main menu..")
                clear_sc('any_key')
                show_menu()
                continue

        else:
            print("Invalid choice. Please try again.")

            continue
    elif choice == '7':
        print("+------------------------------------+")
        print("INTRODUCTION TO WHILE LOOP")
        print("+------------------------------------+")
        
        # Explain the concept
        type_writer("A while loop in Python repeatedly executes a block of code as long as a certain condition is True.")
        type_writer("\nThink of it like this: 'Keep doing this task until the condition stops being True.'")
        
        type_writer("\nBasic structure:")
        type_writer("while condition:")
        type_writer("    # code to repeat")
        
        type_writer("\nExample: Counting from 1 to 5")
        type_writer("count = 1")
        type_writer("while count <= 5:")
        type_writer("    print('Count is', count)")
        type_writer("    count += 1")
        
        type_writer("\nProgression")
        type_writer("- Python sets count = 1")
        type_writer("- Checks if count <= 5 (the condition)")
        type_writer("- If True, it prints the value and adds 1 to count")
        type_writer("- Repeats step 2 until the condition is False")
        
        # Show output to user
        print("\nOutput:")
        count = 1
        while count <= 5:
            print("Count is", count)
            count += 1

        # Option to show code
        show_code = input("\nPress any key to see the code behind this while loop (or just Enter to skip): ")
        if show_code != "":
            code_while = """count = 1
    while count <= 5:
        print('Count is', count)
        count += 1"""
            print("\nCode behind the example:")
            print(code_while)
        
        type_writer("\nWhile loop is also used it give user access to stop the code whenever he/she wants by using the keyword \'continue\' and \'break'")
        type_writer("\n\nWhat \'continue\' does is skips the rest of the current loop and goes back to the top of the loop, checking the condition again(In while loop).")

        type_writer("\n\nAnd \'break\' stops the loop after a certain condition is met, same as continue but what it does is it breaks the code. ")
        
        type_writer("\nLet's see an example of using 'continue' and 'break' in a while loop:")

        type_writer("\nExample of 'continue' and 'break' in a while loop:")

        x = 0
        while True:
            x += 1
            type_writer(f"\nNumber: {x}")

            if x == 3:
                type_writer("Skipping number 3 with 'continue'")
                continue  # skip the rest of this loop iteration

            type_writer(f"Processing number {x}")

            if x == 5:
                type_writer("Stopping the loop with 'break'")
                break  # stop the loop completely

        type_writer("Press Enter if you want to try typing your own While loop code!")
        code_use = input()

        if code_use == "":  # user just pressed Enter
            type_writer("Great! Now you can type your code below. Type 'END' when finished.")
    
            user_code = ""
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                user_code += line + "\n"
    
            type_writer("\nRunning your code...")
            exec(user_code)
            clear_sc('any_key')
            show_menu()
            continue


        else:
            type_writer("You chose not to type code. Returning to menu...")

            type_writer("\nThe loop is now finished!")
            continue
    elif choice == '8':
            print("+------------------------------------+")
            print("INTRODUCTION TO LIST AND DICTIONARY")
            print("+------------------------------------+")
            lst = input("Type 'list' to print List lesson. Type 'dict' to print Dictionary lesson. Type any key to exit --> ")

            if lst == 'list':
                type_writer("Now what is a List?....")
                time.sleep(0.9)
                type_writer("A list is a collection of items in one variable.")
                type_writer("List can store different type of data in one variable.")
                type_writer("A list can hold: ")
                type_writer("\nNumbers(integer) \nTexts(string) \nBooleans(True and False) \nand other lists")
                type_writer("\nBasic example:")
                print()
                type1 = """fruits = ["apple", "banana", "orange"]
scores = [10, 20, 30]
mixed = [1, "hello", True]"""
                type_writer(type1)
                type_writer("\nNow let's try to print the values inside those lists")
                type2 = """fruits = ["apple", "banana", "orange"]
scores = [10, 20 ,30]
mixed = [1, "hello", True]
print(fruits[0])  # apple
print(scores[1])  # 20
print(mixed[2])  # True(Bool)"""
                type_writer(type2)
                type_writer("We are only in the print function of list. ")
                proc = ("Press enter to print the different functions in list: ")
                print("Function \t\t|\t\tKeyword \t\t|\t\tExample \t\t| \t\tOutput")
                print("--------------------------------------------------------------------------------------------------------------------------------------------")
                print("Append \t\t\t\t\tappend() \t\t\t\tlist.append(item) \t\tAdds the selected item \n\t\t\t\t\t\t\t\t\t\t\t\t\t\tinto list at last index")
                print("Insert \t\t\t\t\tinsert() \t\t\t\tlist.insert(1, 99) \t\tInserts item with selected \n\t\t\t\t\t\t\t\t\t\t\t\t\t\tindex")
                print("Remove \t\t\t\t\tremove() \t\t\t\tlist.remove() \t\t\tRemove an item by calling \n\t\t\t\t\t\t\t\t\t\t\t\t\t\tit's value")
                print("Pop \t\t\t\t\tpop.() \t\t\t\t\tlist.pop(0) \t\t\tRemoves an item by index")
                print("Clear \t\t\t\t\tclear() \t\t\t\tlist.clear() \t\t\tRemoves all items")
                print("Index \t\t\t\t\tindex() \t\t\t\tlist.index(1) \t\t\tCalls item by index")
                print("Sort \t\t\t\t\tsort() \t\t\t\t\tlist.sort() \t\t\tSort the list")
                print("Reverse \t\t\t\treverse() \t\t\t\tlist.reverse() \t\t\tReverse the order")
                print("len \t\t\t\t\tlen() \t\t\t\t\tlen(list) \t\t\tPrints number of items")
                list_functions_demo = """
PYTHON LIST FUNCTIONS (EXAMPLE):

nums = [1, 2, 3]
print("Start:", nums)

# 1. append() - add item to end
nums.append(4)
print("append(4):", nums)

# 2. insert() - add item at index
nums.insert(1, 99)
print("insert(1, 99):", nums)

# 3. extend() - add multiple items
nums.extend([5, 6])
print("extend([5, 6]):", nums)

# 4. remove() - remove by value
nums.remove(2)
print("remove(2):", nums)

# 5. pop() - remove last item
nums.pop()
print("pop():", nums)

# pop by index
nums.pop(0)
print("pop(0):", nums)

# 6. clear() - remove all items
temp = nums.copy()
temp.clear()
print("clear():", temp)

# 7. index() - find index of item
nums.append(10)
print("index(10):", nums.index(10))

# 8. len() - counts items
The len() function returns the number of items in a list.

nums = [10, 20, 30, 40]
print(len(nums))

# Output:
# 4

# 9. sort() - sort list
nums.sort()
print("sort():", nums)

# 10. reverse() - reverse list
nums.reverse()
print("reverse():", nums)
"""

                print(list_functions_demo)
                clear_sc('any_key')
                show_menu()
                continue
            elif lst == 'dict':
                type_writer("Now what is a Dictionary?....")
                time.sleep(0.9)
                type_writer("\nA dictionary is a collection of key-value pairs.\nEach key is used to access its corresponding value. Dictionaries are written using curly braces {}.")
                type_writer("\nNow dictionary differs from list because every value is accompanied by a key or keynames")
                notes = """IMPORTANT NOTES:

- Keys must be unique
- Keys are usually strings or numbers
- Values can be any data type
- Dictionaries are mutable (can be changed)"""
                type_writer(notes)

                notes2 = """COMMON FUNCTIONS

len(student)        # number of key-value pairs
student.keys()      # returns all keys
student.values()    # returns all values
student.items()     # returns key-value pairs

+-----------------------------------------------+

KEY POINTS IN USING DICTIONARY

- Dictionaries store data as key : value
- Use {} to create them
- Access values using keys
- Use .get() for safe access"""
                print()
                type_writer(notes2)
                clear_sc('any_key')
                show_menu()
                continue
            else:
                print("Invalid Choice.")
                clear_sc('any_key')
                show_menu()
                continue
    elif choice == '9':
        print("-------------------------------------------------------------------------------")
        print("DEF FUNCTIONS AND PRACTICE CODE EXECUTOR")
        print("-------------------------------------------------------------------------------")
        print("Choose an action from below:")
        print("1. Introduction to Def(User defined functions)")
        print("2. Enter Code Executor")
        print("3. Exit")

        user_choice4 = input("Enter choice: ")

        if user_choice4 == '1':
            def_function = """
PYTHON USER-DEFINED FUNCTIONS (def)

A function is a reusable block of code that performs a specific task.
User-defined functions are created using the 'def' keyword.

Functions help you:
- Reuse code
- Organize programs
- Avoid repetition

--------------------------------------------------

BASIC FUNCTION SYNTAX (ANATOMY)

def function_name(parameters):
    code to run
    return value (optional)

--------------------------------------------------

SIMPLE EXAMPLE (NO PARAMETERS)

def greet():
    print("Hello!")

greet()

Output:
Hello!

--------------------------------------------------

FUNCTION WITH PARAMETERS

def greet(name):
    print("Hello", name)

greet("Alex")

Output:
Hello Alex

--------------------------------------------------

FUNCTION WITH MULTIPLE PARAMETERS

def add(a, b):
    print(a + b)

add(5, 3)

Output:
8

--------------------------------------------------

RETURNING A VALUE

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)

Output:
20

--------------------------------------------------

RETURN VS PRINT

print() shows a value to the screen.
return sends a value back to where the function was called.

--------------------------------------------------

DEFAULT PARAMETERS

def greet(name="User"):
    print("Hello", name)

greet()
greet("Sam")

--------------------------------------------------

FUNCTION WITH LOGIC

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

--------------------------------------------------

CALLING A FUNCTION

You run a function by writing its name followed by parentheses.

function_name()

--------------------------------------------------

IMPORTANT RULES

- Function names should be lowercase
- Use underscores for readability
- Code inside a function must be indented
- A function must be defined before it is called

--------------------------------------------------

SUMMARY

- Use 'def' to create functions
- Functions can take parameters
- Functions can return values
- Functions help keep code clean and reusable
"""
            print(def_function)
            print()
            inp = input("Press enter to try creating you own Python Function!. Type 'END' on a new line when finished:")

            if inp == "":
                print("Type your Python function. Type 'END' on a new line when finished:")

            user_code = ""
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                user_code += line + "\n"

            # Define the function in the current namespace
            exec(user_code)

            # Ask the user which function to run
            func_call = input("Type the function call (e.g., greet()): ")
            try:
                result = eval(func_call)
                if result is not None:
                    print("Output:", result)
            except Exception as e:
                print("Error:", e)
                continue
            else:
                print("You have been directed back to main menu")
                clear_sc('any_key')
                show_menu()
                continue
        elif user_choice4 == '2':
           while True:
                print("Press Enter if you want to try typing your own Python code!")
                print("Or type 'EXIT' to quit.")
                code_use = input()

                if code_use.strip().upper() == "EXIT":
                    print("Goodbye!")
                    clear_sc('any_key')
                    show_menu()
                    continue
                    

                if code_use == "":  # user pressed Enter
                    print("Great! Type your code below. Type 'END' when finished:")

                    user_code = ""
                    while True:
                        line = input()
                        if line.strip().upper() == "END":
                            break
                        user_code += line + "\n"

                    print("\nRunning your code...\n")
                    try:
                        exec(user_code)
                    except Exception as e:
                        print("Error while running your code:", e)

                    input("\nPress Enter to continue...")  # wait before looping again
        elif user_choice4 == '3':
            
                print("You are directed to the main menu..")
                clear_sc('any_key')
                show_menu()
                continue
        else:
        
            print("You are directed to the main menu..")
            clear_sc('any_key')
            show_menu()
            continue
            
                    
    elif choice == '10':
        type_writer("THANK YOU FOR USING MY SYSTEM. COMEBACK AGAIN!......")
        break
    else:
        type_writer("INVALID CHOICE.")
        clear_sc('any_key')
        show_menu()
        continue

                        

        
       
        



            

