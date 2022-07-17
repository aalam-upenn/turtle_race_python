from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

def move_forward():
    tim.pendown()
    tim.forward(20)
def move_backward():
    tim.pendown()
    tim.backward(20)
def head_counterclockwise():
    tim.left(10)
def head_clockwise():
    tim.right(10)
def clear_all():
    tim.penup()
    tim.clear()
    tim.home()

my_screen.listen()
my_screen.onkey(key = "w", fun = move_forward)
my_screen.onkey(key = "s", fun = move_backward)
my_screen.onkey(key = "a", fun = head_counterclockwise)
my_screen.onkey(key = "d", fun = head_clockwise)
my_screen.onkey(key = "c", fun = clear_all)


my_screen.exitonclick()