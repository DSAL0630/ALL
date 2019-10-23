# how to make a list 
favMovies = ["Joker" , "Endgame" , "Batman"]
# print the whole list 
print(favMovies)
# print individuals
print(favMovies[0])
# to add you can use append or insert
# append adds to the end
favMovies.append("Kill Bill")
print(favMovies)
# insert will put the item wherever you want
favMovies.insert(1, "JOJO")
print(favMovies)
# how to remove items 
# remove by name or by index
# remove by name use remove
favMovies.remove("Kill Bill")
print(favMovies)
# favMovies.remove("Ted")
# pop will remove the last item unless an index is given
favMovies.pop()
print(favMovies)
favMovies.pop(1) # will remove whatever is in index 1
print(favMovies)

# get the length of a list
# this is a function
# the function name is len
print("My list has " + str(len(favMovies)) + " items")
favMovie = input("What is your favorite movie? ")
favMovies.append(favMovie)
print(favMovies)
print(favMovies[len(favMovies) - 1])

# loop through a list
count = 1

for movie in favMovies:
	print("My number " + str(count) + " movie is " + movie)
	count = count + 1 

numList = [1, 3, 5, 7, 9, 11, 13, 15]
# challenge: Loop through the list and add all the numbers together, then print the sum

total = 0
for number in numList:
	total = total + number
	
print("The sum is " + str(total))


if "Endgame" in favMovies:
	favMovies.remove("Endgame")
	print("removed")
else:
	print("not in the list")
