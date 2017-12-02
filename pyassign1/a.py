import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")

sun =turtle.Turtle()
sun.color("yellow")
sun.shape("blank")
sun.speed(0)
sun.screen.delay(0)
sun.up()
sun.backward(10)
sun.left(90)
sun.backward(5)
sun.left(-90)
sun.down()
sun.begin_fill()

for i in range(20):
    sun.forward(20)
    sun.left(126)
    
sun.end_fill() 

def away(t,r):    
    t.up()
    t.left(90)
    t.forward(r)
    t.left(-90)
    t.down()

mer = turtle.Turtle()
mer.color("cyan")
mer.shape("circle")
mer.shapesize(0.122)
away(mer,13)

ven = turtle.Turtle()
ven.color("gold")
ven.shape("circle")
ven.shapesize(0.6052)
away(ven,24)

ear = turtle.Turtle()
ear.color("turquoise")
ear.shape("circle")
ear.shapesize(0.6378)
away(ear,33)

mar = turtle.Turtle()
mar.color("salmon")
mar.shape("circle")
mar.shapesize(0.1699)
away(mar,50)

jup = turtle.Turtle()
jup.color("lightgreen")
jup.shape("circle")
jup.shapesize(0.71492)
away(jup,170)

sat = turtle.Turtle()
sat.color("tan")
sat.shape("circle")
sat.shapesize(0.60268)
away(sat,318)

def dc(t,r,n):
    l=n*r*math.pi/1800
    t.forward(l)
    t.left(-0.1*n)

for t in [mer,ven,ear,mar,jup,sat]:
    t.screen.delay(0)
    t.speed(10)
    
for i in range(10000000000000000000000000):
    dc(mer,13,10)
    dc(ven,24,5)
    dc(ear,33,4)
    dc(mar,50,2)
    dc(jup,170,1)
    dc(sat,318,0.4)

wn.exitonclick()
