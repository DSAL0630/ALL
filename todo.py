print("Welcome to the To Do List")
todoList = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")
	taskList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	choice = input("Make your choice: ")
	if choice == "q":
		break
	elif choice == "a":
		# add am item to the list
		item = input("What would you like to add to your list: ")
		todoList.append(item)
		print(str(numList)item)
		pass
	elif choice == "r":
		# remove an item from the list
		pass
	elif choice == "p":
		# print the list
		print(item)
		pass
	else:
		print("That is not a choice")