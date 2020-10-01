import turtle

def draw_stripe(size):
    pam.forward(size)
    pam.right(90)

screen = turtle.Screen()
pam = turtle.Turtle()

# for i in range(50):
#    draw_stripe(i*5)

for i in range(100):
    draw_stripe(i*3)
    pam.left(90/100)

screen.exitonclick()