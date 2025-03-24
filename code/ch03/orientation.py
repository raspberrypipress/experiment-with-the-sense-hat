from sense_hat import SenseHat

sense = SenseHat()

while True:
    pitch, roll, yaw = sense.get_orientation().values()
    print(f"pitch={pitch}, roll={yaw}, yaw={roll}")
