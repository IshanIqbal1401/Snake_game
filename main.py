from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.bgcolor('black')

screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.tracer(0)
timmy = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(timmy.up, 'Up')
screen.onkey(timmy.down, 'Down')
screen.onkey(timmy.left, 'Left')
screen.onkey(timmy.right, 'Right')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    timmy.move()
    # collision with food
    if timmy.head.distance(food) < 15:
        food.refresh()
        timmy.extend()
        score_board.update_score()
    # collision with wall
    if timmy.head.xcor() > 280 or timmy.head.xcor() < -280 or timmy.head.ycor() > 280 or timmy.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()
    # collision with tail
    for segments in timmy.segments[1:]:
        if timmy.head.distance(segments) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
