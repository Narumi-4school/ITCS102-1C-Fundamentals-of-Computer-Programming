temp = eval(input("Enter temperature --> "))

if temp >= 1 and temp <= 20:  		 	 	 	 print("The temperature is considered extremely cold")
elif temp >= 21 and temp <= 30 : 	 	 	 	 print("The temperature is moderately cold")
elif temp >= 31 and temp<= 37:	 	 	 	 	 print("The temperature is normal")
elif temp >= 38 and temp <= 45: 		  		 print("The temperature is hot")
elif temp >= 45 and temp <= 50: 	 		 	 print("The temperature is boiling hot") 
elif temp >= 50:	 	 	 	  		 print("The temperature is dangerous")
else: 
  		 	 	 	  	  	print("The temperature is invalid")