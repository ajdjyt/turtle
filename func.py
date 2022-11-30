import turtle
def left(dude):
    dude.backward(1)


def right(dude):
    dude.forward(1)


def up(dude):
    dude.left(90)
    dude.forward(1)
    dude.right(90)


def down(dude):
    dude.right(90)
    dude.forward(1)
    dude.left(90)