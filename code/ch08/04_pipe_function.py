from sense_hat import SenseHat
from random import randint

sense = SenseHat()
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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

matrix = gen_pipes(matrix)
matrix = flatten(matrix)
sense.set_pixels(matrix)