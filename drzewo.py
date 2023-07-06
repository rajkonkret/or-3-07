import turtle

t = turtle.Turtle()
t.speed(-1)
t.setheading(90)
t.penup()
t.goto(0, -200)
t.pendown()


def draw(t, len_):
    if len_ == 0: return
    nt = t.clone()
    nt.forward(50)
    nt.left(20)
    draw(nt, len_ - 1)
    nt.right(40)
    draw(nt, len_ - 1)


draw(t, 7)
window = turtle.Screen()
window.exitonclick()
