import turtle

def draw_square(size):
    for i in range(4):
        pam.forward(size)
        pam.left(90)

screen = turtle.Screen()
pam = turtle.Turtle()

sizes = [20, 40, 60, 80, 100]
for i in sizes:
    draw_square(i)
    pam.penup()
    pam.right(90)
    pam.forward(10)
    pam.right(90)
    pam.forward(10)
    pam.right(180)
    pam.pendown()



screen.exitonclick()
