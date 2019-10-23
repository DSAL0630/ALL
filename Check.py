# Name: Diego Saldivar
# Period: 4

# variable declaration and assignment 
# examples
myNum = 12 # integer type
myString = "12" # string type
myNum + 3 # OK
myString + "3" # not OK
print(myString + "3") # OK

# make a variable and assign it the value of your favorite movie
# print "my favorite movie is " followed by the variable
myMovie = "Joker"
myFav = print("my favorite movie is " + str(myMovie))

# while loops
# example - print from 1 to 10
x = 1
while x <= 10:
	print(x)
	x = x + 1

# count down from 100 using while loop
x = 100
while x>= 0:
	print(x)
	x = x - 1

# String concatenation
# means putting two strings together
# example
myName = "Arthur"
print("Hello " + myName)

# input 
# example
yourName = input("What is your name? ")
print("Hello " + yourName + " have a nice day")
number = input("Enter a number: ")
number = int(number) + 10
print ("The number is " + str(number))
# ask for two numbers, add them and print the sum
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("The sum is: " + str(num1 + num2))

# if / else statements
# example
num = int(input("Enter a number: "))
if num > 100:
	print("Your number is more than 100")
elif num == 100:
	print("Your number is equal to 100")
else:
	print("Your number is less than 100")

# ask if today is your birthday
# if yes print happy birthday

bDay = input("Is today your birthday? ")
if bDay == "yes":
	print("Happy birthday")
else:
	print("Have a nice day anyway")