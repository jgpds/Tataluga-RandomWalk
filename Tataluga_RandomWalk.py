from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("red", "pink")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = ["right", "left", "forward", "back"]
index = 3
tim.speed(20)
tim.pensize(10)

# meu método (método da angela yu abaixo)

for _ in range(200):
    tim.color(random.choice(colours))
    if random.choice(direction) == "right":
        tim.right(90)
        tim.forward(20)
    elif random.choice(direction) == "left":
        tim.left(90)
        tim.forward(20)
    elif random.choice(direction) == "forward":
        tim.forward(20)
    else:
        tim.backward(20)

# modo alternativo
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.right(random.choice(directions))
#     tim.forward(20)


# modo alternativo 2 usando .setheading
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.setheading(random.choice(directions))
#     tim.forward(20)

screen.exitonclick()
