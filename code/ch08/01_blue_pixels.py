from sense_hat import SenseHat
sense = SenseHat()

RED = (255, 0, 0)
BLUE = (0, 0, 255)

matrix = [[BLUE for column in range(8)] for row in range(8)]

def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened

matrix = flatten(matrix)
sense.set_pixels(matrix)