from turtle import *
from random import *


def turtleRectangle(x, y, width, height):
    penup()
    setx(x)         
    sety(y)
    seth(0)         
    pendown()     
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    penup()          

def turtleRectangleFill(x, y, width, height):          #Function for filling the rectangles
    penup()
    setx(x)         
    sety(y)
    seth(0)         
    pendown()
    begin_fill()   
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()
    penup()    

def turtlePolygon(x, y, nside, sidelength):
    setx(x)         
    sety(y)
    seth(0)      
    pendown()       
    angle = 180 - ((nside-2)*180/nside)   #Formula for finding the angle of a regular polygon
    for i in range(nside):
        forward(sidelength)
        left(angle)                     
    penup()

def drawRect(x1, y1, x2, y2):
    turtleRectangleFill(x1, y1, x2-x1, y2-y1)

def Carpet(n, x1, y1, x2, y2):
    drawRect((2 * x1 + x2) / 3, (2 * y1 + y2) / 3, ((x1 + 2 * x2) / 3) - 1, ((y1 + 2 * y2) / 3) - 1 )

    if(n < 4):                  #Number of recursions for the carpet

    #Code for 8 squares for recursion in the output
            Carpet(n + 1, x1, y1 , (2 * x1 + x2) / 3, (2 * y1 + y2) / 3)                
            Carpet(n + 1, (2 * x1 + x2) / 3, y1, (x1 + 2 * x2) / 3, (2 * y1 + y2) / 3)
            Carpet(n + 1, (x1 + 2 * x2) / 3, y1 , x2, (2 * y1 + y2) / 3)
            Carpet(n + 1,  x1 , (2 * y1 + y2) / 3, (2 * x1 + x2) / 3, (y1 + 2 * y2) / 3)
            Carpet(n + 1, (x1 + 2 * x2) / 3, (2 * y1 + y2) / 3, x2 , (y1 + 2 * y2) / 3)
            Carpet(n + 1, x1, (y1 + 2 * y2) / 3, (2 * x1 + x2) / 3,  y2)
            Carpet(n + 1, (2 * x1 + x2) / 3, (y1 + 2 * y2) / 3, (x1 + 2 * x2) / 3,  y2)
            Carpet(n + 1, (x1 + 2 * x2) / 3, (y1 + 2 * y2) / 3, x2,  y2)

def turtleSierpinskiCarpet(x, y, width):
    Carpet(1, x, y, x+width, y+width);
    

def turtleShapes():
    penup()
    turtlePolygon(-300, 200, 100, 3)
    turtleRectangle(-200, 200, 50, 100)
    turtlePolygon(-100, 200, 3, 50)
    turtlePolygon(0, 200, 4, 50)
    turtlePolygon(100, 200, 5, 50)
    turtlePolygon(225, 200, 6, 50)
    turtlePolygon(350, 200, 7, 50)
    turtleSierpinskiCarpet(-100, -300, 300)
    pendown()
                                                    
def additionQuiz():
    print ("Starting Addtion Quiz...")
    while True:
        x = randint(0, 9)        
        y = randint(0, 9)
        print (x, "+", y)
        value = input("?")          #Checking for the input
        if (value != " "):              #Checking for whitespace
            try:
                val = int(value)        #Converting value to int and checking for exception
                if (val == x+y):
                    print ("Correct!")
                else:
                    print ("The correct answer is: ", x+y)       #Printing the correct answer
            except ValueError:
                print ("Invalid Number!")       #If Exception raised printing invalid number            
        else:
            break

if __name__ == "__main__":
    tracer(0)               #Removing the tracing to speed up the drawing process
    speed(0)                #Maximising the speed of the animations to speed up the drawing process
    # turtleRectangle(-100,0,100,100)
    # turtlePolygon(110,0,12,50)
    # turtleSierpinskiCarpet(-100,-300,243)
    turtleShapes()
    mainloop()                  #For keeping the outout open after the animation
    additionQuiz()            #Adding this as the mainloop to keep the final output onscreen