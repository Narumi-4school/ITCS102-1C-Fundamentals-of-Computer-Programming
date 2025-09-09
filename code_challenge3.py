name = input ("What is your name? --> ")
fee = eval(input("How much is your fare fee? --> "))
ocp = input("Are you a student? ( yes / no )")
new_fee = fee * 0.2
dis = fee - new_fee

if ocp == "yes" or ocp == "YES": 	 		  	print("Hi",name,"your discounted fare is",dis)
else:  		 	 	 	 	 	 	print("Hi",name,"You are only eligible for the regular fare fee") 
 







		 	 	  	