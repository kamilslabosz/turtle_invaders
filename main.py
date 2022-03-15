import random
from turtle import Screen

from base_manager import BaseManager
from invader_manager import InvaderManager
from player import Player

screen = Screen()
screen.setup(width=800, height=800)
screen.title("Turtle invaders")
screen.tracer(0)

base_manager = BaseManager()
invader_manager = InvaderManager()
player = Player()

screen.listen()
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")
screen.onkey(player.shoot, "Up")

game_is_on = True

base_manager.create_bases()
invader_manager.create_army()
while game_is_on:
    screen.update()

    invader_manager.move_to_side()
    invader_manager.bullet_down()
    player.bullet_up()

# checking distance between each bullet and each invader
    for invader in invader_manager.all_invaders:

        for bullet in player.all_bullets:
            if bullet.distance(invader) < 20:
                invader_manager.all_invaders.remove(invader)
                player.all_bullets.remove(bullet)
                bullet.goto(x=0, y=-500)
                invader.goto(x=0, y=-500)

        # check if player lost
        for base in base_manager.all_bases:
            if base.distance(invader) < 50:
                player.goto(0, 0)
                game_is_on = False
                player.color('black')
                player.ht()
                player.write('Game Over', align="center", font=("Courier", 80, "normal"))

        # random chance to shoot for invaders
        if random.randint(1, 20001) == 1:
            invader_manager.shoot(x=invader.xcor(), y=invader.ycor())

    # checking if bullets hit any of the bases
    for base in base_manager.all_bases:

        for bullet in invader_manager.all_bullets:
            if bullet.distance(base) < 50:
                # base.counter_down()
                bullet.goto(x=0, y=-500)
                invader_manager.all_bullets.remove(bullet)

        for bullet in player.all_bullets:
            if bullet.distance(base) < 50:
                # base.counter_down()
                bullet.goto(x=0, y=-500)
                player.all_bullets.remove(bullet)

    # checking if bullets are out of bounds
    for bullet in player.all_bullets:
        y = bullet.ycor()
        if y > 450:
            player.all_bullets.remove(bullet)

    for bullet in invader_manager.all_bullets:
        y = bullet.ycor()
        if y < -450:
            invader_manager.all_bullets.remove(bullet)

    # checking and changing direction of invaders
    if invader_manager.direction == "right":
        for invader in invader_manager.all_invaders:
            if invader.xcor() > 349:
                invader_manager.move_down()
                invader_manager.direction = 'left'

    if invader_manager.direction == "left":
        for invader in invader_manager.all_invaders:
            if invader.xcor() < -349:
                invader_manager.move_down()
                invader_manager.direction = 'right'

    # checking if player won
    if not invader_manager.all_invaders:
        player.goto(0, 0)
        player.ht()
        player.color('black')
        player.write('You won!', align="center", font=("Courier", 80, "normal"))
        game_is_on = False


screen.exitonclick()
