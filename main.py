import turtle
#from time import sleep
#from func import up,down,left,right
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


scrn=turtle.Screen()
scrn.bgcolor("Grey")
dude=turtle.Turtle()
dude.left(90)
turtle.delay(0)
#dude.ht()
dude.speed(0)
#turtle.tracer(0,0) #removes screen updates, requires turtle.update to be called to draw
dude.down()
dude.color("orange")
scrn.onkey(up,"w")
scrn.onkey(down,"s")
scrn.onkey(left,"a")
scrn.onkey(right,"d")
scrn.onkey(quit,"q")
scrn.listen()
#sleep(10)
turtle.done()