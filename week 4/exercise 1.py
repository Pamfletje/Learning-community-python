import turtle

def draw_square(size):
    for i in range(4):
        pam.forward(size)
        pam.left(90)

screen = turtle.Screen()
pam = turtle.Turtle()

for i in range(5):
    draw_square(20)
    pam.penup()
    pam.forward(40)
    pam.pendown()

screen.exitonclick()


