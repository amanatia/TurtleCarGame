from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_car()
        
    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(x=310, y= random.randint(-250, 250))
        car.shapesize(1,2)
        self.cars.append(car)
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def move(self):
        for car in self.cars:
            car.goto(car.xcor() - self.car_speed, car.ycor())
        
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        
    