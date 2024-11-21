import turtle

screen = turtle.Screen()
screen.bgcolor("Cyan")
screen.title("Polygon using turtle")

t=turtle.Turtle()
t.pencolor("Blue")
t.pensize(5)
t.shape("arrow")

for _ in range(6):
    t.forward(100)
    t.right(60)

t.hideturtle()
turtle.done()