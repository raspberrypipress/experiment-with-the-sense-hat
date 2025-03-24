from sense_hat import SenseHat

sense = SenseHat()

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

    print(f"x={x}, y={y}, z={z}")
