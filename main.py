import random
import time
import turtle

MIN_RACERS = 2
MAX_RACERS = 10
WIDTH, HEIGHT = 400, 400
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def getNumberOfRacers():
    racers = 0
    while True:
        racers = input(f"Enter number of racers ({MIN_RACERS} - {MAX_RACERS}): ")
        if racers.isdigit():
            racers = int(racers)
            if MIN_RACERS <= racers <= MAX_RACERS:
                break
            else:
                print(f"Please enter a number between {MIN_RACERS} - {MAX_RACERS}")
        else:
            print("Please enter a valid number!!!")

    return racers


def createTurtle(colors):
    turtles = []
    spacingx = WIDTH / (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH / 2 + (i + 1) * spacingx, -HEIGHT / 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = createTurtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 15)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT / 2 - 10:
                return colors[turtles.index(racer)]

def intiTurtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!!')


racers = getNumberOfRacers()
print(f"Total number of racers are {racers}")
intiTurtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
print(f"Colors of turtles are {colors}")

winner = race(colors)
print(f"Winning turtle color is: {winner}")







