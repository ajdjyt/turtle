import turtle
from time import sleep
scrn=turtle.Screen()
scrn.bgcolor("Grey")
dude=turtle.Turtle()
dude.color("orange")
dude.down()
x=0
while x==0:
    try:
        print("Enter direction to move ")
        print("0.exit")
        print("1.Up")
        print("2.Down")
        print("3.Left")
        print("4.Right")
        dir=int(input(": "))
    except:
        print("Enter a number")
        continue
    if dir==0:
        break
    elif dir==1:
        dude.left(90)
        dude.forward(1)
        dude.right(90)
    elif dir==2:
        dude.right(90)
        dude.forward(1)
        dude.left(90)
    elif dir==3:
        dude.backward(1)
    elif dir==4:
        dude.forward(1)
    else:
        print("Enter a valid option")
        continue

#sleep(10)
turtle.done()