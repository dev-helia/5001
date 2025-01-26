import turtle

def draw_square(myTurtle, sideLength):
    myTurtle.forward(sideLength)  #side 1
    myTurtle.right(90) 
    myTurtle.forward(sideLength)  #side 2
    myTurtle.right(90)
    myTurtle.forward(sideLength)  #side 3
    myTurtle.right(90)
    myTurtle.forward(sideLength)  #side 4
    myTurtle.right(90)

def main():
    t = turtle.Turtle()
    draw_square(t, 100)

if __name__ == "__main__":
    main()
