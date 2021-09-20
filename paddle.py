#create a paddle class

from turtle import Turtle



MOVEDISTANCE = 20

#create a paddle
#paddle will be made up of a stretched square


class Paddle(Turtle):

    def __init__(self, x_pos):
        self.xpos = x_pos
        if self.xpos > 0:
            self.front_edge = self.xpos - 10
        else:
            self.front_edge = self.xpos + 10
        self.ypos = 0
        self.edges = []
        self.top = 0
        self.bottom = 0
        super().__init__()
        self.shape("square")
        self.penup()
        self.resizemode("user")
        self.shapesize(5, 1, 1)
        self.color("white")
        self.speed("fastest")
        self.goto(self.xpos, self.ypos)
        
    #move the paddle up by 20
    #replace ypos value with new value

    def move_up(self):
        current_ypos = self.ycor()
        self.ypos = current_ypos + 20
        self.goto(self.xpos, self.ypos)
        self.top = self.ypos + 50
        self.bottom = self.ypos -50
        self.paddle_edges()

    def move_down(self):
        current_ypos = self.ycor()
        self.ypos = current_ypos - 20
        self.goto(self.xpos, self.ypos)
        self.top = self.ypos + 50
        self.bottom = self.ypos -50
        self.paddle_edges()

    def paddle_edges(self):
        self.edges = []
        for i in range((self.bottom - 10), (self.top + 10), 1):
            self.edges.append(i)





    

    
        

        



    
        

    



    
    




