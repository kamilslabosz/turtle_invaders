from turtle import Turtle


class InvaderManager:

    def __init__(self):
        self.all_invaders = []
        self.direction = "right"
        self.speed = 1.0
        self.all_bullets =[]

    def create_army(self):
        for num in range(0, 40):
            new_invader = Turtle('turtle')
            new_invader.shapesize(stretch_len=2, stretch_wid=2)
            new_invader.penup()
            new_invader.right(90)

            row = num % 10

            new_invader.goto(x=-350+(row*50), y=150+50*(num//10))
            self.all_invaders.append(new_invader)

    def move_to_side(self):
        if self.direction == 'right':
            move = 0.5
        elif self.direction == 'left':
            move = -0.5

        for invader in self.all_invaders:
            x = invader.xcor()
            y = invader.ycor()
            invader.goto(x=x+move*self.speed, y=y)

    def move_down(self):
        for invader in self.all_invaders:
            x = invader.xcor()
            y = invader.ycor()
            invader.goto(x=x, y=y-3)
            self.speed += 0.001

    def shoot(self, x, y):
        new_bullet = Turtle('square')
        new_bullet.color('red')
        new_bullet.shapesize(stretch_len=0.5, stretch_wid=1)
        new_bullet.penup()
        new_bullet.goto(x=x, y=y)
        self.all_bullets.append(new_bullet)

    def bullet_down(self):
        for bullet in self.all_bullets:
            x = bullet.xcor()
            y = bullet.ycor()
            bullet.goto(x, y-1)


