from turtle import Turtle, width


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.new_score = open("saved_scores.txt", mode="r")
        self.content = self.new_score.read()
        self.high_score = self.content
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}, High Score : {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))

    def save_score(self):
        with open("saved_scores.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            self.save_score()
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}, High Score : {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))

    def add_to_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}, High Score : {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))
