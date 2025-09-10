print("Konnichiwa, Welcome to 1Cmangareader.com")
print("Select your genre")
print("1. Action")
print("2. Horror")
print("3. Romance")

genre = input("Enter your choice (1/2/3):")

if genre == '1':
    print("Your chosen genre is Action")
    print("Select year range")
    print("1990")
    print("2000")
    print("2010")
elif genre == '2':
    print("Your chosen genre is Horror")
    print("Select year range")
    print("1990")
    print("2000")
    print("2010")
elif genre == '3':
    print("Your chosen genre is Romance")
    print("Select year range")
    print("1990")
    print("2000")
    print("2010")

year = input("Enter year range (1990/2000/2010): ")

if year == '1990':
    print("You selected year range 1990")
    print("Select length: ")
    print("1. Short")
    print("2. Medium")
    print("3.Long")

elif year ==  '2000':
    print("You selected year range 2000")
    print("Select length: ")
    print("1. Short")
    print("2. Medium")
    print("3.Long") 
elif year == '2010':
    print("You selected year range 2010")
    print("Select length: ")
    print("1. Short")
    print("2. Medium")
    print("3.Long") 

length = input("Enter length (1/2/3): ")

if length == '1':
    print("Your chosen length is Short")
elif length == '2':
    print("Your chosen length is Medium")
elif length == '3':
    print("Your chosen length is Long")

if genre == '1'and year == '2000' and length == '3':
    print("Here is my recommendations:")
    print("Fullmetal Alchemist")
    print("D.Gray-man")
    print("Gantz")
    print("Air Gear")
    print("Eyeshield 21")

else:
    print("Sorry i dont have any recommendation for you")    


