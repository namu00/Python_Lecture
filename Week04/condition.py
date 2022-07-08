import turtle
t = turtle

swidth,sheight = 500,500

t.shape('turtle')
t.setup(width = swidth + 50,height = sheight +50)
t.screensize(swidth,sheight)
t.penup()
t.goto(0,-sheight/2)
t.pendown()
t.speed(10000)

for radius in range(1,250):
    if radius % 6 == 0: t.pencolor('red')
    elif radius % 5 == 0: t.pencolor('orange')
    elif radius % 4 == 0: t.pencolor('yellow')
    elif radius % 3 == 0: t.pencolor('green')
    elif radius % 2 == 0: t.pencolor('blue')
    elif radius % 1 == 0: t.pencolor('navyblue')
    else : t.pencolor('purple')
    
    t.circle(radius)
t.done()