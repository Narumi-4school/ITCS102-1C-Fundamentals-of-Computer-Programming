from getpass import getpass
username = 'dash'
pword = 'dwyestilo'
 
u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")

if (u == username) and (p == pword) :		 	 	 	 print ("Acess Granted")
else: 		 	 	 	 	 	 	    	 print ("Acess Denied")