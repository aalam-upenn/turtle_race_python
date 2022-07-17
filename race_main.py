from turtle import Turtle, Screen
from random import randint
my_screen = Screen()
my_screen.setup(width=800, height=500)
number_of_players = my_screen.textinput(title = "Total Players", prompt= "How many players will play the game? (Up to 6): ")
player_choice = {}
for num in range(int(number_of_players)):
    k = my_screen.textinput(title = "Name", prompt = f"Enter Player {num+1} name: ")
    v = my_screen.textinput(title = "Choice", prompt = f"Enter Player {num+1} turtle color ('red', 'orange', 'yellow', 'green', 'blue', 'purple'): ")
    player_choice[k] = v

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_cor = 100
i = 0
race_on = False
for color in colors:
    color = Turtle(shape="turtle")
    color.color(colors[i])
    all_turtles.append(color)
    i+=1
    color.penup()
    color.goto(-380, y_cor)
    y_cor -= 30

if player_choice:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor()>= 360:
            race_on = False
            winning_turtle = turtle.pencolor()
            for name in player_choice:
                if winning_turtle == player_choice[name]:
                    print(f"{name} has won! The {winning_turtle} turtle is the winner")
                else:
                    print(f"{name} has lost! The {winning_turtle} turtle is the winner")

        turtle.forward(randint(0,10))


my_screen.exitonclick()