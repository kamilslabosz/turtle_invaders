from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.goto(0, -350)
        self.left(90)
        self.all_bullets = []

    def go_right(self):
        if self.xcor() < 350:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
        else:
            pass

    def go_left(self):
        if self.xcor() > -350:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())
        else:
            pass

    def shoot(self):
        new_bullet = Turtle('square')
        new_bullet.color('blue')
        new_bullet.shapesize(stretch_len=0.5, stretch_wid=1)
        new_bullet.penup()
        new_bullet.goto(x=self.xcor(), y=-320)
        self.all_bullets.append(new_bullet)

    def bullet_up(self):
        for bullet in self.all_bullets:
            x = bullet.xcor()
            y = bullet.ycor()
            bullet.goto(x, y+1)