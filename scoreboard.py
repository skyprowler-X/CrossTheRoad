from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_player = 1
        self.penup() 
        self.color("Black")
        self.hideturtle()
        self.goto((-230, 270))
        self.write("Level = 1" , align="center", font=('Courier', 14, 'normal'))

    def update_score(self):    
        self.clear()   
        self.score_player += 1
        self.write(f"Level = {self.score_player}" , align="center", font=('Courier', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER" , align="center", font=('Courier', 50, 'normal'))
        self.goto(0, -40)
        self.write(f"Your score: {self.score_player}" , align="center", font=('Courier', 30, 'normal'))
        
