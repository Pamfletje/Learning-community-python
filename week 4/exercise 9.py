import turtle

def draw_star(degrees):
    for i in range(5):
        pam.forward(100)
        pam.right(degrees)

screen = turtle.Screen()
pam = turtle.Turtle()

draw_star(144)

screen.exitonclick()
