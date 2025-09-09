price = eval(input("Enter the price: "))
qtty = eval(input("Quantity: "))

cost = price * qtty
discount = cost * 0.10
new_cost = cost - discount

if cost >= 100 :	 					print ("Here is the total with the 10% discount",new_cost)				
else:								print("Hello your total is not eligible for the discount here is the total",cost)

 	