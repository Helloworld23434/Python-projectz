num= int(input("Enter your number: "))
if (num<0):
	print("The number is negative")
elif(num>0):
	if(0<num<10):
		print("Its between zero to 10")
	elif(10<num<20):
			print("The number is between 10 to 20")
	elif(num>20):
		print("The number is greater than 20")
else:
	print("The number is 0")	
