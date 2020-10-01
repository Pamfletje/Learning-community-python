import turtle

def draw_square(size):
    for i in range(4):
        pam.forward(size)
        pam.left(90)

screen = turtle.Screen()
pam = turtle.Turtle()

for i in range(20):
    draw_square(50)
    pam.left(360/20)


screen.exitonclick()