from turtle import Turtle

POINT_FONT = ("Courier", 20, "normal")
FONT = ("Courier", 10, "normal")

class State_board(Turtle):
    def __init__(self):
        super(State_board, self).__init__()
        self.penup()
        self.hideturtle()
        self.point = 0


    def update_point(self):
        self.clear()
        self.goto(300,250)
        self.write(f"{self.point} / 50", align="center", font=POINT_FONT)

    def get_point(self):
        self.point += 1
        self.update_point()

    def show_state(self, x, y, state_name):
        self.goto(x, y)
        self.write(state_name, align="center", font=FONT)
