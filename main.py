import turtle
import random
import time

# set up the game window
screen = turtle.Screen()
screen.title("Turtle Race Track")
screen.bgcolor("black")
screen.setup(width=800, height=500)
screen._root.iconbitmap("icon.ico")

# stop auto screen updates so animation looks smooth
screen.tracer(0)

# create drawing turtle for track lines
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.color("white")
drawer.speed("fastest")

# draw start line text and line
drawer.goto(-350, -200)
drawer.write("START", align="center", font=("Arial", 14, "bold"))

drawer.goto(-300, -200)
drawer.pendown()
drawer.forward(600)

# draw finish line text and line
drawer.penup()
drawer.goto(-350, 200)
drawer.write("FINISH", align="center", font=("Arial", 14, "bold"))

drawer.goto(-300, 200)
drawer.pendown()
drawer.forward(600)

# draw vertical lane lines
for i in range(6):
    drawer.penup()
    drawer.goto(-300 + i * 120, -200)
    drawer.setheading(90)
    drawer.pendown()
    drawer.forward(400)

# create turtle for showing messages
announcement = turtle.Turtle()
announcement.hideturtle()
announcement.penup()
announcement.color("white")

# function to show text on screen
def show_message(message, y=0, size=24):
    announcement.clear()
    announcement.goto(0, y)
    announcement.write(message, align="center", font=("Arial", size, "bold"))
    screen.update()

# list of turtle colors
colors = ["pink", "blue", "red", "yellow", "green"]
racers = []

# starting x position for lanes
start_x = -300

# create racers and place them in lanes
for index, color in enumerate(colors):
    racer = turtle.Turtle(shape="turtle")
    racer.penup()
    racer.color(color)
    racer.setheading(90)

    # place turtle in center of its lane
    lane_x = -300 + index * 120 + 60
    racer.goto(lane_x, -180)

    racers.append(racer)

# update screen after placing turtles
screen.update()

# reset turtles back to start position
def reset_race():
    for index, racer in enumerate(racers):
        lane_x = -300 + index * 120 + 60
        racer.goto(lane_x, -180)
        racer.setheading(90)

# main race loop
def run_race():
    winner = None

    # keep racing until someone wins
    while winner is None:
        for racer in racers:
            # move turtle by random small steps
            distance = random.randint(1, 10)
            racer.forward(distance)

            screen.update()
            time.sleep(0.01)

            # check if turtle reached finish line
            if racer.ycor() >= 180:
                winner = racer
                break
    return winner

# start the game flow
def start_game():
    reset_race()
    show_message("Turtle Race Begins!")
    time.sleep(1)

    # countdown before race starts
    for count in ["3", "2", "1", "GO!"]:
        show_message(count)
        time.sleep(1)

    announcement.clear()

    winner = run_race()
    winner_color = winner.pencolor().capitalize()

    # show winner message
    show_message(
        f"{winner_color} Turtle Wins!\nPress R to Restart",
        y=0,
        size=24
    )

# restart game when user presses R
def restart():
    show_message("Restarting...", y=0, size=20)
    time.sleep(1)
    start_game()

# listen for keyboard input
screen.listen()
screen.onkey(restart, "r")

# start the first game
start_game()

# keep window open
screen.mainloop()
