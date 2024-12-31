from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        
    
    def reset_position(self):
        self.goto(STARTING_POSITION)
        
        
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        
    def finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    def collided(self, car):
        # car.shapesize() -> tuple: (car.stratch_wid, car.stretch_len, outline) 
        car_height = car.shapesize()[0] * 20 # this way I get the height in pixels
        car_width = car.shapesize()[1] * 20 
        
        car_x = car.xcor()
        car_y = car.ycor()
        if (self.xcor() + self.shapesize()[0] * 10 < car_x - car_width / 2 or 
        self.xcor() - self.shapesize()[0] * 10 > car_x + car_width / 2 or 
        self.ycor() + self.shapesize()[1] * 10 < car_y - car_height / 2 or 
        self.ycor() - self.shapesize()[1] * 10 > car_y + car_height / 2):
            return False
        return True
        

