import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()
leonardo.left(45)
leonardo.forward(200)
leonardo.circle(50,220)

leonardo.stamp()
leonardo.right(180)
leonardo.circle(50,220)
leonardo.forward(200)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

for element in [0, 1, 2, 3, 4, 5]:
    leonardo.color(colors[element % len(colors)])
    if element % 2 == 0:
        leonardo.forward(50)
    leonardo.forward(50)
    leonardo.left(60)
paper.exitonclick()
