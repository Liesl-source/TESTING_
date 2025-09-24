import turtle
spiral=turtle.Screen()
spiral.bgcolor("lightblue")
spiral.title("Turtle")
pen=turtle.Turtle()
size=0
while True:
    for i in range(4):
        pen.fd(size+1)
        pen.left(90)
        size-=5
    size=size+1
    if size>100:
        break 