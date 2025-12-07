#----------COMPILER PROGRAM-----------
import os
import random
import sys
inv = {}
def show_menu():
  print("WELCOME TO MY MINI-INVENTORY PROGRAM")
  print("-------------------------------------")
  print("Choose an action below:")
  print("1. Add an inventory")
  print("2. Add items to inventory")
  print("3. View all inventories")
  print("4. Modify itmes in inventory")
  print("5. Search inventory")
  print("6. Delete an inventory")
  print("X. Exit")
def option_2(inv_id):
    if inv_id in inv:
        item = input("Enter the item you want to add to the inventory --> ")
        category = input("Enter the category of item --> ")
        inv[inv_id].append({"item" : item , "category" : category})
        print(f"'{item}' added to '{inv_id}' inventory")
    else:
        print("No such inventory exists. Please create one first.")
def option_4(inv_id):
  if inv_id in inv:
    for inv_names, items in inv.items():
      print(f"Inventory Title/Name - {inv_names} \nItems - {items}")

show_menu()


while True:
   max = input("Input chosen action: ")

   if max == '1':
     print("ADD AN INVENTORY")
     print("------------------------------")
     inv_id = input("Create a name for the inventory --> ")
     print("INVENTORY ADDED TO COLLECTION")
     inv[inv_id] = []
     continue


   elif max == '2':
     print("ADD AN ITEM TO INVENTORY")
     print("---------------------------")
     inv_id = input("Enter the inventory where you want to add items --> ")
     option_2(inv_id)
     continue
   elif max == '3':
     print("VIEW ALL INVENTORIES")
     print("---------------------------")
     if not inv:
       print("No inventories found")
     else:
       for inv_names, items in inv.items():
         print(f"Inventory Title/Name - {inv_names} \nItems - {items}")
     continue
   elif max == '4':
     print("MODIFY ITEMS IN INVENTORY")
     print("------------------------------")
     select = input("Enter the inventory title/name you want to manage --> ")
     if select in inv:
       option_4(select)
     else:
       print("No inventories found")
       continue