number = eval(input("Enter any number -->"))
factorial = 1
for x in range(number, 0, -1):
   factorial *= x

print("The factorial of",number,"is",factorial)
