from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('verdana', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open('hs.txt') as hs:
            self.high_score = int(hs.read())
        self.score = 0
        self.hideturtle()
        self.setpos(0, 260)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('hs.txt', 'r+') as hs:
                hs.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def refresh(self):
        self.score += 1
        self.update_scoreboard()
