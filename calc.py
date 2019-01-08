#!/usr/bin/python3

### functions

def counting(x,y):
	return x + y

def subtraction(x,y):
	return x - y

def multiplication(x,y):
	return x * y

def deljenje(x,y):
	return x / y

### print

print("Select the operand")
print("================")
print("Counting")
print("substraction")
print("Multiplication")
print("Division")


entrance = input("Enter 1,2,3 or 4")
num1 = int(input("Please enter 1st number"))
num2 = int(input("Please enter 2ns number"))

### check

for i in entrance:

	if i == "1":
		print(num1, "+",num2,"=", counting(num1,num2)) ## counting

	elif i == "2":
		print(num1, "+",num2,"=",subtraction(num1,num2)) ## substraction

	elif  i == "3":
		print(num1, "+",num2,"=",multiplication(num1,num2)) ## multiplication

	elif  i == "4":
		 print(num1, "+",num2,"=", division(num1,num2)) ## subtraction

	else:
		print("Wrong entrance. Please enter 1,2,3 or 4!")
	break
