from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()

    def create_snake(self):
        for strt in starting_positions:
            new_s = Turtle("square")
            new_s.color("white")
            new_s.penup()
            new_s.goto(strt)
            self.segments.append(new_s)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)

    # def snake_left(self):
    #     self.segments[0].left(90)
    #     self.move()
    #
    # def snake_right(self):
    #     self.segments[0].right(90)
    #     self.move()

