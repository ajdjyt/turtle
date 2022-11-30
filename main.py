import turtle
def left():
    global dude
    dude.left(90)
    dude.forward(10)
    dude.right(90)
    print(dude.position())


def right():
    global dude
    dude.right(90)
    dude.forward(10)
    dude.left(90)
    print(dude.position())


def up():
    global dude
    dude.forward(10)
    print(dude.position())


def down():
    global dude
    dude.backward(10)
    print(dude.position())

#Initialise screen and set colours
scrn=turtle.Screen()
scrn.bgcolor("Grey")
dude=turtle.Turtle()
dude.color("orange")
#Set cursor to point up
dude.left(90)
#Disable vfx delay of 10ms
turtle.delay(0)
#dude.ht() #Hide the turtle head
#Set speed to 0 for max speed
dude.speed(0)
#turtle.tracer(0,0) #removes screen updates, requires turtle.update to be called to draw
dude.down()
#Set keys to call functions
scrn.onkey(up,"w")
scrn.onkey(down,"s")
scrn.onkey(left,"a")
scrn.onkey(right,"d")
scrn.onkey(quit,"q")
#Start listening for key presses
scrn.listen()
turtle.done()