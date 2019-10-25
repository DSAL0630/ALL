print("Welcome to HangMan")
myWord = "saphire"
myString = "saphire"
myList = list(myString)
guessList = []
for letter in myList:
	guessList.append("_")
	
print(guessList)


while True:
	if guessList == ['s', 'a', 'p', 'h', 'i', 'r', 'e']:
		print("Good job you figured out the word!")
		break
	def display(HANGMANPICS, missedLetters):
		print(HANGMANPICS[len(missedLetters)])
		print()

		print('missedLetters:', end=' ')
		for letter in missedLetters:
			print(letter, end=' ')
		print()
	
	letter = input("Type a letter: ")
	if letter in myWord:
		print("Letter is in the word")
	if letter == "s":
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

HANGMANPICS = ['''  
   +---+
   |   |
       |
       |
       |
       |
       |
   ======= ''' , '''
   
   +---+
   |   |
   0   |
       |
       |
       |
       |
   ======= ''' , '''

   +---+
   |   |
   0   |
   |   |
       |
       |
       |
   ======= ''' , '''

   +---+
   |   |
   0   |
  /|   |
       |
       |
       |
   ======= ''' , '''

   +---+
   |   |
   0   |
  /|\  |
       |
       |
       |
   ======= ''' , '''

   +---+
   |   |
   0   |
  /|\  |
  /    |
       |
       |
   ======= ''' , '''

   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
       |
   ======= ''']