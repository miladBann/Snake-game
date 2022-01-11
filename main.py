from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score


end = False

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

milo = Snake()
food = Food()
score = Score()
##############################################
# movement


while end == False:
    screen.update()
    time.sleep(0.1)
    milo.move()
    screen.onkey(fun=milo.move_right, key="d")
    screen.onkey(fun=milo.move_left, key="a")
    screen.onkey(fun=milo.move_up, key="w")
    screen.onkey(fun=milo.move_down, key="s")

    if milo.segments[0].distance(food) < 15:
        score.add_to_score()
        milo.extend()
        food.refresh()

    for segment in milo.segments:
        if segment == milo.segments[0]:
            pass
        elif milo.segments[0].distance(segment) < 5:
            score.reset()
            milo.reset()

    if milo.segments[0].xcor() > 300 or milo.segments[0].xcor() < -300 or milo.segments[0].ycor() > 300 or milo.segments[0].ycor() < -300:
        score.reset()
        milo.reset()


screen.exitonclick()
