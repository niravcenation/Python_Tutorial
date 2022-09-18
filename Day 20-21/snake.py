from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.pointers = []
        self.create_snake()
        self.head = self.pointers[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            if positions == (0, 0):
                self.first_pointer(positions)
            else:
                self.add_pointer(positions)

    def first_pointer(self, positions):
        pointer = Turtle("square")
        pointer.color("blue")
        pointer.penup()
        pointer.goto(positions)
        self.pointers.append(pointer)

    def add_pointer(self, positions):
        pointer = Turtle("square")
        pointer.color("white")
        pointer.penup()
        pointer.goto(positions)
        self.pointers.append(pointer)

    def extend(self):
        # adds a one slice at the end
        self.add_pointer(self.pointers[-1].position())

    def move(self):
        for pointer_number in range(len(self.pointers) - 1, 0, -1):
            new_x = self.pointers[pointer_number - 1].xcor()
            new_y = self.pointers[pointer_number - 1].ycor()
            self.pointers[pointer_number].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
