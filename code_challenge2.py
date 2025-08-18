amount = eval(input("Enter amount to deposit: "))

print ("Here is a breakdown of your deposit: ")

thou = amount // 1000
tc = amount % 1000
 

fh = tc // 500 
fhc = tc % 500

th = fhc // 200 
thc = fhc % 200

oneh = thc // 100
onehc = thc % 100

fifty = onehc // 50
fifty_change = onehc % 50

twenty = fifty_change // 20
twch = fifty_change % 20

tens = twch // 10 
tch = twch % 10

fives = tch // 5 
fc = tch % 5 

ones = fc // 1 
onec = fc % 1

 


print (thou," - 1000")
print (fh," - 500")
print (th," - 200")
print (oneh," - 100")
print (fifty," - 50")
print (twenty," - 20")
print (tens," - 10")
print (fives," - 5")
print (ones," - 1")










 

