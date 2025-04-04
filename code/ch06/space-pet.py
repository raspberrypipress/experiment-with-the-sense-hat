from sense_hat import SenseHat
import time

sense = SenseHat()

p = (204, 0, 204) # Pink
g = (0, 102, 102) # Dark Green
w = (200, 200, 200) # White
y = (204, 204, 0) # Yellow
e = (0, 0, 0) # Empty

pet1 = [
 e, e, e, e, e, e, e, e,
 p, e, e, e, e, e, e, e,
 e, p, e, e, p, e, p, e,
 e, p, g, g, p, w, w, e,
 e, g, g, g, w, y, w, y,
 e, g, g, g, g, w, w, e,
 e, g, e, g, e, g, e, e,
 e, e, e, e, e, e, e, e
 ]
pet2 = [
 e, e, e, e, e, e, e, e,
 p, e, e, e, e, e, e, e,
 e, p, e, e, p, e, p, e,
 e, p, g, g, p, w, w, e,
 e, g, g, g, w, y, w, y,
 e, g, g, g, g, w, w, e,
 e, e, g, e, g, e, e, e,
 e, e, e, e, e, e, e, e
 ]

def walking():
    for i in range(10):
        sense.set_pixels(pet1)
        time.sleep(0.5)
        sense.set_pixels(pet2)
        time.sleep(0.5)

sense.clear(0, 0, 0)
sense.set_pixels(pet1)
while True:
    x, y, z = sense.get_accelerometer_raw().values()
    if x >= 2 or y >= 2 or z >= 2:
        break
walking()
