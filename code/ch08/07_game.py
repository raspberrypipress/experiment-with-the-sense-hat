from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
game_over = False

x = 0
y = 0

matrix = [[BLUE for column in range(8)] for row in range(8)]

def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened

def gen_pipes(matrix):
    for row in matrix:
        row[-1] = RED
    gap = randint(1, 6)
    matrix[gap][-1] = BLUE
    matrix[gap + 1][-1] = BLUE
    matrix[gap - 1][-1] = BLUE
    return matrix

def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i + 1]
        row[-1] = BLUE
    return matrix

def move_astronaut(event):
    global x, y
    sense.set_pixel(x, y, BLUE) # Hide the astronaut
    if event.action == "pressed":
        if event.direction == "up" and y > 0:
            y -= 1
        elif event.direction == "down" and y < 7:
            y += 1
        elif event.direction == "right" and x < 7:
            x += 1
        elif event.direction == "left" and x > 0:
            x -= 1
    check_collision()
    sense.set_pixel(x, y, YELLOW) # Show the astronaut

def check_collision():
    global game_over
    if matrix[y][x] == RED:
        game_over = True

sense.stick.direction_any = move_astronaut

while True:
    matrix = gen_pipes(matrix)
    for i in range(4):
        sense.set_pixels(flatten(matrix))
        check_collision()
        if game_over:
            sense.show_message('Game Over')
            raise SystemExit
        matrix = move_pipes(matrix)
        sense.set_pixel(x, y, YELLOW) # Show the astronaut
        sleep(1)
