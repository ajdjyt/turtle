import turtle
def left():
    global dude
    dude.backward(1)


def right():
    global dude
    dude.forward(1)


def up():
    global dude
    dude.left(90)
    dude.forward(1)
    dude.right(90)


def down():
    global dude
    dude.right(90)
    dude.forward(1)
    dude.left(90)