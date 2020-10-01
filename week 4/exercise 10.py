import turtle

def draw_star(degrees):
    for i in range(5):
        pam.forward(100)
        pam.right(degrees)


screen = turtle.Screen()
pam = turtle.Turtle()

for i in range(5):
    draw_star(144)
    #pam.penup()
    pam.forward(300)
    #pam.pendown()
    pam.right(144)



screen.exitonclick()