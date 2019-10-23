print("Welcome to HangMan")
myWord = "saphire"
lList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
sList = ["_", "_", "_", "_", "_", "_", "_"]
print(sList)

while True:
	letter = input("Type a letter: ")
	if letter in myWord:
		print("Letter is in the word")
	elif letter == "s":
		guessList[0] = "s"
	elif letter == "s":
		guessList[0] = "a"
	elif letter == "s":
		guessList[0] = "p"
	elif letter == "s":
		guessList[0] = "h"
	elif letter == "s":
		guessList[0] = "i"
	elif letter == "s":
		guessList[0] = "r"
	elif letter == "s":
		guessList[0] = "e"	
	else:
		print("Letter is not in the word")
		
		





















# How to turn a string into a list
myString = "arizona"
myList = list(myString)
print(myList)

# how to create a list with _ where the letters go
guesslist = []
for a in myList:
	guessList.append("_")

print(guessList)

# how to replace a specific item in a list
# so say the user types r for guess you would 
guessList[1] = "r"
print(guessList)