import turtle

def draw_square(degrees):
    for i in range(4):
        pam.forward(100)
        pam.right(degrees)

screen = turtle.Screen()
pam = turtle.Turtle()

for i in range(20):
    draw_square(90)
    pam.left(360/20)



screen.exitonclick()