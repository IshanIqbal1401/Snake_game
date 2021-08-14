from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_UP = 90
MOVE_DOWN = 270
MOVE_RIGHT = 0
MOVE_LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != MOVE_DOWN:
            self.head.setheading(MOVE_UP)

    def down(self):
        if self.head.heading() != MOVE_UP:
            self.head.setheading(MOVE_DOWN)

    def left(self):
        if self.head.heading() != MOVE_RIGHT:
            self.head.setheading(MOVE_LEFT)

    def right(self):
        if self.head.heading() != MOVE_LEFT:
            self.head.setheading(MOVE_RIGHT)

    def add_segment(self,position):
        new_segments = Turtle(shape='square')
        new_segments.penup()
        new_segments.color('white')
        new_segments.goto(position)
        self.segments.append(new_segments)


    def extend(self):
        self.add_segment(self.segments[-1].position())

