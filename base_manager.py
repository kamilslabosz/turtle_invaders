from turtle import Turtle


class BaseManager:

    def __init__(self):
        self.all_bases = []
        
    def create_bases(self):
        for num in range(4):
            new_base = Turtle('square')
            new_base.color('orange')
            new_base.shapesize(stretch_len=5, stretch_wid=5)
            new_base.penup()
            new_base.goto(x=-225+num*150, y=-230)
            self.all_bases.append(new_base)

