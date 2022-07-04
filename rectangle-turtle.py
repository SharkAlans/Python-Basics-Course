import turtle
turtle = turtle.Pen()
turtle.shape('turtle')
def Rectangle():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)

def Go(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


for i in range(10):
    turtle.circle(50)
    turtle.left(36)

