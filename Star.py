import turtle
turtle.Screen().bgcolor("pink")
base=turtle.Turtle()
#first triangle
base.forward(100)
base.left(120)

base.forward(100)
base.left(120)
base.forward(100)

base.penup()
base.right(150)
base.forward(50)
#secound triangle
base.pendown()
base.right(90)
base.forward(100)

base.right(120)
base.forward(100)

base.right(120)
base.forward(100)


turtle.done()