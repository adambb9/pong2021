from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        x_pos, y_pos = 0, 275
        self.goto(x_pos, y_pos)
        self.player1score = 0
        self.player2score = 0
        self.update_score()

    #score board writes to screen but doesnt update
    def update_score(self):
        self.write(F"{self.player1score} : {self.player2score}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
    def increase_player1_score(self, num):
        self.player1score += num
        self.clear()
        self.update_score()
    
    def increase_player2_score(self, num):
        self.player2score += num
        self.clear()
        self.update_score()