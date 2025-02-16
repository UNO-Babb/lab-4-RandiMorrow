#TurtleGraphics.py
#Name: Randi Morrow
#Date: 2/16/25
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(xena, sides):
    for s in range(sides):
        xena.forward(50)
        xena.right(360/sides)

def fillCorner(frank, corner):
    #draw big square
    drawSquare(frank, 100)
    
    if corner == 1: 
        frank.begin_fill()
        drawSquare(frank, 50)
        frank.end_fill()
    
    elif corner == 2:
        frank.forward(50)
        frank.begin_fill()
        drawSquare(frank, 50)
        frank.end_fill()

    elif corner == 3:
        frank.forward(100)
        frank.right(90)
        frank.forward(50)
        frank.begin_fill()
        drawSquare(frank, 50)
        frank.end_fill()
        
    elif corner == 4:
        frank.forward(50)
        frank.right(90)
        frank.forward(50)
        frank.begin_fill()
        drawSquare(frank, 50)
        frank.end_fill()
        
        
def squaresInSquares(myTurtle, num):
    size = 200 
    for i in range(num):
        drawSquare(myTurtle, size) 
    
        size -= 20
        myTurtle.penup()
        myTurtle.goto(myTurtle.xcor() + 10, myTurtle.ycor() - 10)
        myTurtle.pendown() 
        

    
def main():
    myTurtle = turtle.Turtle()

    # I tested all of these below and they all worked! 

    #drawSquare(myTurtle, 100)
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
    # drawPolygon(myTurtle, 3) triangle 
    
    
    # fillCorner(myTurtle, 3) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
