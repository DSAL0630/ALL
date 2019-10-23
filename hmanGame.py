print("Welcome to HangMan")
myWord = "saphire"
myString = "saphire"
myList = list(myString)
guessList = []
for a in myList:
	guessList.append("_")
	
print(guessList)
while True:
	if guessList == ['s', ]
	letter = input("Type a letter: ")
	if letter in myWord:
		print("Letter is in the word")
	elif letter == "s":
		guessList[0] = "s"
		print(guessList)
	elif letter == "a":
		guessList[1] = "a"
		print(guessList)
	elif letter == "p":
		guessList[2] = "p"
		print(guessList)
	elif letter == "h":
		guessList[3] = "h"
		print(guessList)
	elif letter == "i":
		guessList[4] = "i"
		print(guessList)
	elif letter == "r":
		guessList[5] = "r"
		print(guessList)
	elif letter == "e":
		guessList[6] = "e"
		print(guessList)	
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

secretWord = "christmas"
secretWord = list(secretWord)
hangmanList = ['''
+===+
    |
    |
    |
   ===''' , "second" , "Third" ]

misses = 0

while misses < 7:
	guess = input("Guess a letter: ")
	if guess in secretWord:
		# loop through secretword and change my guesslist at the correct indexes
		print("letter is in the word")
	else:
		misses += 1


print("Game Over")