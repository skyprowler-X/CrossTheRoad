import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car_list = CarManager()

screen.listen()
screen.onkeypress(player.move_up, 'w')


car_spaw = 0
game_is_on = True
while game_is_on:

    time_speed = 0.1           
    time.sleep(time_speed)
    screen.update()
  
    car_list.create_cars()
    car_list.move()

    if player.ycor() >= FINISH_LINE_Y:
            player.go_back()
            score.update_score()
            car_list.incresing_speed()
            

    for car_from_list in car_list.list_cars:
        if car_from_list.distance(player) <= 20:
            score.game_over()
            game_is_on = False

        elif car_from_list.xcor() <= -340:
            car_list.list_cars.remove(car_from_list)
    car_spaw += 1




screen.exitonclick()

