"""
money =int(input('교환할 돈은 얼마?'))

m500, m100, m50, last = 0,0,0,0
m500 = money//500
print("500원 짜리: ==> %d 개" %m500)
m100 = (money - m500*500)//100
print("100원 짜리: ==>  %d 개" %m100)
m50 = (money - m500*500 - m100*100)//50
print("50원 짜리: ==> %d 개" %m50)
last = money - (m500*500 + m100*100 + m50*50)
print("바꾸지 못한 돈: ==> %d 원" %last)
"""

import turtle
import random

t = turtle.Turtle()

swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r,g,b,angle,dist,curX,curY = [0]*7

t.shape('turtle')
t.pensize(pSize)
t.setup(width = swidth +30, height = sheight + 30)
t.screensize(swidth,sheight)

while True:
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor((r,g,b))
    
    angle = random.randrange(0,360)
    dist = random.randrange(1,100)
    t.left(angle)
    t.forward(dist)
    curX = t.xcor()
    curY = t.ycor()
    
    if(-swidth / 2 <=curX and curX <= swidth/2) and (-sheight / 2 <=curY and curY <= sheight/2) :
         pass
    else :
        t.penup()
        t.goto(0,0)
        t.pendown()
        
    exitCount +=1
    if exitCount >= 5 :
        break
    
turtle.done()
t.exitonclick()