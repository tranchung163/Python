from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__ (self):
        self.starting_position = [(0,0), (-20,0), (-40,0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        

    def create_snake(self):
        for position in self.starting_position:
            self.add_segment(position)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move_forward(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    
    # def extend_snake(self):
    #     self.starting_position.append(self.segments[-1])
    #     self.add_segment(self.starting_position[-1].position())

    def extend_snake(self):
        new_segment = self.segments[-1].position()
        self.add_segment(new_segment)
        

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
