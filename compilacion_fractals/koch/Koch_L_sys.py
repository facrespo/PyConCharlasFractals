#!/usr/bin/env python3
import turtle

koch = 'FRFRF' # axiom for Koch snowflake
iterations = 3 #the number of generations
startLength = 200 #Length of the generation 0 line

#pick the pen up and move cursor to a good starting point
turtle.penup()
turtle.setpos(-startLength*3/2,startLength*3/2/2)
turtle.speed(0)

#make the L-System we want to process
for i in range(iterations):
    koch = koch.replace("F","FLFRFLF")

turtle.pendown() 
#draw line in black, fill sky blue
turtle.color('black','skyblue') 
turtle.begin_fill() 

for move in koch: 
    if move == "F":
        turtle.forward(startLength / (3 ** (iterations - 1)))
    elif move == "L":
        turtle.left(60)
    elif move == "R":
        turtle.right(120)

turtle.end_fill() #fill any enclosed areas
turtle.mainloop()

