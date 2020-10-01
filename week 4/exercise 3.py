import turtle

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


screen = turtle.Screen()
tess = turtle.Turtle()

draw_poly(tess, 8, 50)

screen.exitonclick()
