import turtle
from time import sleep
from func import up,down,left,right
scrn=turtle.Screen()
scrn.bgcolor("Grey")
dude=turtle.Turtle()
dude.color("orange")
dude.down()
x=0
while x==0:
    scrn.onkey(up(dude),key="w")
    scrn.onkey(down(dude),key="s")
    scrn.onkey(left(dude),key="a")
    scrn.onkey(right(dude),key="d")
    scrn.onkey(quit(),key="q")
#sleep(10)
turtle.done()