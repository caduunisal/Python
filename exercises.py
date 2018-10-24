#http://www.practicepython.org




def insline (num):
	print ("[ " + num + " ]" + "-" * 100)


insline('1')
# 1. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = raw_input("Please enter your name: ")
type(name)
age = input("Please enter your age: ")
type(age)
print ("Hello " + name + "!\nYour age is " + str(age) + " years old!\n")



insline('2')
# 2. Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
number = input ("Please enter an integer number: ")
type(number)
if number % 2:
	print ("Odd Number!\n")
else:
	print ("Even Number!\n")



insline('3')
# 3. Take a list, say for example this one:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#and write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in a:
	if num<5:
		print (num)
