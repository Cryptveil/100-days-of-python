import turtle
import os
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Space Invaders")
screen.bgcolor("black")

# Register the shapes for the player, enemy, and bullet
turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("bullet.gif")

# Create the player turtle
player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.goto(0, -250)
player.direction = "stop"

# Create a list of enemies
enemies = []
for i in range(5):
    enemy = turtle.Turtle()
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    enemy.goto(-200 + i*100, 250)
    enemy.dx = 4
    enemies.append(enemy)

# Create the bullet turtle
bullet = turtle.Turtle()
bullet.shape("bullet.gif")
bullet.penup()
bullet.speed(0)
bullet.goto(0, -250)
bullet.dy = 10
bullet.state = "ready"

# Set up the score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Define the player's movements
def move_left():
    player.direction = "left"
    player.dx = -5

def move_right():
    player.direction = "right"
    player.dx = 5

def stop():
    player.direction = "stop"
    player.dx = 0

# Bind the keyboard events
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkey(stop, "Up")

# Define the collision function
def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 30:
        return True
    else:
        return False

# Main game loop
while True:
    # Move the player
    player.setx(player.xcor() + player.dx)
    if player.xcor() < -280:
        player.direction = "stop"
        player.dx = 0
        player.setx(-280)
    if player.xcor() > 280:
        player.direction = "stop"
        player.dx = 0
        player.setx(280)

    # Move the enemies
    for enemy in enemies:
        enemy.setx(enemy.xcor() + enemy.dx)

        # Check for a collision between the bullet and enemy
        if is_collision(bullet, enemy):
            # Reset the bullet
            bullet.goto(0, -250)
            bullet.dy = 10
            bullet.state = "ready"

            # Reset the enemy
            enemy.goto(-200 + random.randint(0, 4)*100, 250)

            # Update the score
            score += 10
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        # Check for a collision between the player and enemy
        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

# Move the bullet
        if bullet.state == "fire":
            bullet.sety(bullet.ycor() + bullet.dy)

        # Check if the bullet has gone off the screen
        if bullet.ycor() > 275:
            bullet.goto(0, -250)
            bullet.dy = 10
            bullet.state = "ready"

        # Check for keyboard input to fire the bullet
        if player.direction != "stop":
            if bullet.state == "ready":
                bullet.state = "fire"
                bullet.goto(player.xcor(), player.ycor())

        # Add a delay to control the frame rate
        turtle.delay(20)

# Quit Turtle
    turtle.bye()


