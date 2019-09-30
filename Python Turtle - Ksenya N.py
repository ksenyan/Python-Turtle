import turtle
t = turtle.Turtle()
screen = turtle.Screen()
t.penup()
t.goto(-500, 200)
t.speed(1000)
t.pensize(2)
screen.bgcolor("darkseagreen")
#Here, we set up the turtle and shortened it to "t".
#We put it into the middle of the screen and made it's speed a bit faster than default.

def mount() : #this draws triangles 
    t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(300)

def drawTrunk() :
    t.pencolor("saddlebrown")
    t.fillcolor("saddlebrown")
    t.begin_fill()
    t.setheading(270)
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.end_fill()

def leafR (): #This draws one triangle
    t.forward(40)
    t.left(135)
    t.forward(80)
    t.right(135)
    
def leafL ():
   t.forward(80)
   t.left(135)
   t.forward(40)
   t.right(135)
   
def drawLeavesR ():    
    t.setheading(0)
    t.forward(40)
    for steps in range(3) :
        leafR()  #this draws half of a tree by drawing the triangle 3 times.
        
def drawLeavesL ():
    t.setheading(225)
    for steps in range(3) :
        leafL() #draws second half, mirrored
    t.setheading(0)
    t.forward(40) #connects everything, shape gets filled in.
    
def drawTree (x,y): #this function runs the smaller functions.
    t.goto (x,y)
    t.pendown()
    drawTrunk()
    t.pencolor("darkgreen")
    t.fillcolor("green")
    t.begin_fill()
    drawLeavesR() 
    drawLeavesL()
    t.end_fill()
    t.penup() #I used pen up/down so when we start a new
             #tree, there isn't anything connecting them.
t.pendown()
t.setheading(315)
t.pencolor("gray")
t.fillcolor("gray")
t.begin_fill()
for triangles in range (3) : #draw 5 triangles
    mount()
t.setheading(180)
t.forward(500) #draw a line at the bottom to connect
t.end_fill() 
t.penup()

#Now we want to colour the sky - same shape, upside down

t.goto(-500, 200)
t.pendown()
t.setheading(315)
t.pencolor("lightblue")
t.fillcolor("lightblue")
t.begin_fill()
for triangles in range (3) : #draw 5 triangles, just like mountains
    mount()
t.left(135)             #this time we go above to fill the shape
t.forward(300)
t.left(90)
t.forward(1280)
t.end_fill()
t.penup()

  #time to draw tress in all the different spots!
drawTree(155,135)
drawTree(-300,100)
drawTree(-10,70)
drawTree(250, 50)
drawTree(100, -75)   
drawTree(-150, 25)
drawTree(-200, -75)
drawTree(-400, -90)
drawTree(425, 90)
drawTree(400, -100)
           #this part draws 3 trees, spread out.
           #now that the trees are drawn, we'll do the pond.

t.goto(-490,-245)
t.pensize(35)
t.pencolor("darkblue")
t.fillcolor("cornflowerblue")
t.setheading(45)
def pond(): #bush will appear as a part of a squiggly line across the screen
    t.pendown()
    counterR = int(0)
    counterL = int(0)

    while counterR != 10 : #top half of squiggly line
        t.forward(9)
        t.right(9)
        counterR = counterR+1
    while counterL != 10 : #bottom half of squiggly line
        t.forward(9)
        t.left(9)
        counterL = counterL+1
    t.penup()
t.begin_fill()
for waves in range(6) :
    pond ()
t.right(135) #these movements draw the bottom of the pond to fill it.
t.forward(500)
t.right(90)
t.forward(1000)
t.right(90)
t.forward(500)
t.end_fill()

#I want to add accent waves, so we'll use the squiggly line code again

t.pencolor("darkblue")
t.pensize(15)
t.setheading(315)
def wave(x,y) :
    t.goto(x,y)
    counter = int(0)
    t.pendown()
    t.left(90)
    while counter != 10 : #top half of squiggly line
        t.forward(9)
        t.right(9)
        counter = counter+1
    t.penup()
    
wave(-400, -375) #We repeat the half circle a few more times to add accents.
wave(250, -380)
wave(-70, -350)

#Last step is to add a sun and clouds!

t.goto(-490,400)
t.setheading(270)
t.pencolor("yellow")
t.fillcolor("yellow")
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()

t.setheading(45)
t.pencolor("white")
t.fillcolor("white")
t.pensize(20)

t.goto(-430, 350)
pond()
t.goto(-50, 370)             #The shape of the pond waves would look ok as clouds...
pond()
t.goto(220, 300)
pond()

print ("All done!") #If we got here, it's successfull.               
