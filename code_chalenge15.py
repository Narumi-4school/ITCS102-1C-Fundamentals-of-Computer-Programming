import os

print("DLL STUDENT INFORMATION SYSTEM")
print("------------------------------------")
stud_info = {}

while True:
    print("SELECT THE FOLLOWING OPTIONS ")
    print("A - Add Student record ")
    print("B - Search Student ")
    print("C - Edit Student record ")
    print("D - Delete Student record ")
    print("E - Print all Student info ")
    print("F - Export Data ")
    print("G - Exit System ")
    
    choice = input("Select option from A - G --> ").lower().strip()

    if choice == 'a':
        print("ADD STUDENT RECORD")

        stud_id = input("Input Student ID: ")
        first_name = input("Type your first name: ").UPPER()
        mid_name = input("Type your middle name: ").UPPER()
        last_name = input("Type your last name: ").UPPER()
        section = ("Type your section: ").UPPER()
        email = ("Type your email: ")
        
        stud_info[stud_id] = [first_name, mid_name, last_name, section, email]
        print("DATA SAVE SUCCESSFULLY")
        os.system(cls)
        continue
    elif choice == 'b':
        pass
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        pass
        continue
    elif choice == 'e':
        pass
        continue
    elif choice == 'f':
        pass
        continue
    elif choice == 'g':
        print("System exit")
        break
    else:
        print("Invalid choice")
        continue

        
        
