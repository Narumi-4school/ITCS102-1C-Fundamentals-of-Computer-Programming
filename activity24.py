from activity23_1 import *

print("WELCOME TO MY COMPILER PROGRAM")
name = input("Hi visitor, What is your name? --> ")

isCont = True

while isCont == True:
    choice = input("Select from A - E --> ").lower()

    if choice == 'a':
        name = input("Please state your name: ")
        GreetWithName(name)
        continue
    elif choice == 'b':
        number = eval(input("Input any number: "))
        print(f"Factirual of {number} is {Factorial(number)}")
        continue
    elif choice == 'c':
        GetTriangle()
        continue
    elif choice == 'e':
        print("Program Terminated...")
        break
    else:
        print("Invalid choice")