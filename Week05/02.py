import turtle
import random
t = turtle
r = random

myTurtle,tX,tY,tColor,tSize,tShape = [None]*6
shapeList = []
playerTurtles=[]
swidth,sheight = 500,500

if __name__ == "__main__":
    t.setup(width = swidth + 50,height = sheight + 50)
    t.screensize(swidth,sheight)
    
    shapeList = t.getshapes()
    for i in range(0,100):
        r.shuffle(shapeList)
        myTurtle = t.Turtle(shapeList[0])
        tX = r.randrange(-swidth/2,swidth/2)
        tY = r.randrange(-sheight/2,sheight/2)
        ra = r.random() 
        g = r.random()
        b = r.random()
        tSize = r.randrange(1,3)
        playerTurtles.append([myTurtle,tX,tY,tSize,ra,g,b])
        
    for tList in playerTurtles:
        myTurtle = tList[0]
        myTurtle.color((tList[4],tList[5],tList[6]))
        myTurtle.penolor((tList[4],tList[5],tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1],tList[2])
    t.done()
    turtle.done()