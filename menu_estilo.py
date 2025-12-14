# Welcome to my Python Functions Compiler Programm -------
import os 
import time

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
def Fl_Triangle():
    
def clear_sc(any_key):
    any_key = input("Press any key to exit... ")
    os.system('cls')
def try_print():
    print("\nLet's practice the print() function!")
    print("Type the text you want to print (without quotes).")

    user_input = eval(input("Your value: "))
    
    print("\nHere\'s what your print() would show:")
    print(user_input) # safely prints the data



def show_menu():
    print("+------------------------------------+")
    print("WELCOME TO My PYTHON COMPILER SYSTEM")
    print("+------------------------------------+")

    name = input("What is your name? .....  ")

    print("Hello",name,"Choose an action from 1 - 9 --> ")
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
         print("x = 5 \nx += 5 # adds and updates the variable \nprint(x) \n10")
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
            a = input("Do you want to see the code behind that? (Y/N) ").lower()
            if a == 'y':
                print("def conditional_stat(val):\n\tage = val # gets the value from the def function \nif age >= 18: #checks if age is greater than or equal to 18 \n\tprint('You are an adult') # Prints if True \nelse: \n\tprint('You are still a minor') # Prints if false")
                continue
            else:
                print("Okay! Thank you for using this system.")
                break
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
            print("3. Loop with math")
            print("4. Value checker")
            print("5. Exit")
            print()
            user_choice3 = input("Enter choice --> ")
            
            if user_choice3 == '1':
                
            
            
            
            pass
            
            
    
        
        
        
        
            
        
            
            
            
            
            
            
            
            
            
            
            
            

