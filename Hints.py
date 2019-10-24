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

# how to loop through a string and replace letters
mystery = list("halloween")
guessList = list("_________")

guessList = input("Guess a letter: ")
index = 0

for letter in mystery:
	if letter == guess:
		guessList[index] = guess
	index += 1

print(guessList)