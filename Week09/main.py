import myTurtle
import turtle

inStr = ''
swidth,sheight = 300,300
tx,ty,tangle,tsize = [0]*4

turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.speed(5)

inStr = myTurtle.getStr()

for ch in inStr:
    tx,ty,tangle,tsize = myTurtle.getXYAS(swidth,sheight)
    r,g,b = myTurtle.getRGB()
    
    turtle.goto(tx,ty)
    turtle.left(tangle)
    
    turtle.pencolor((r,g,b))
    turtle.write(ch,font = ('맑은고딕',tsize,'bold'))
    
turtle.done()