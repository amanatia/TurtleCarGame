import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Road Game")
screen.tracer(0)

timmy = Player()

screen.listen()
screen.onkey(timmy.go_up, "Up")

car = CarManager()

score = Scoreboard()

finished = False

count = 0
game_is_on = True
while game_is_on:
    
    count += 1

    if count == 6:
        car.create_car()
        count = 0
        
   
    car.move() 
    
    for i in car.cars:
        if timmy.collided(i):
            game_is_on = False
            score.game_over()
            
    
    
            
    #Detect successful crossing
    if timmy.finished():
        timmy.reset_position()
        car.increase_speed()
        score.increase_level()
       
      
    time.sleep(0.1)
    screen.update()

screen.exitonclick()