from turtle import *
t = Turtle()
screen = t.getscreen()

def writeName():
	name = screen.textinput("name box", "What is your name?")
	t.write(name, move=True, align="left", font=("Times New Roman",30,"normal"))
	screen.listen()

def move():
	t.forward(10)

def move1():
	t.right(90)

def move2():
	t.left(90)

screen.onkey(writeName, "w")
screen.onkey(move, "Up")
screen.onkey(move1, "Right")
screen.onkey(move2, "Left")
screen.listen()
screen.mainloop()