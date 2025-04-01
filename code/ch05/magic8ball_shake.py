import random
import time
from sense_hat import SenseHat

sh = SenseHat()

sh.show_message("Ask a question?")

replies = [
'Signs point to yes',
'Without a doubt',
'You may rely on it',
'Do not count on it',
'Looking good',
'Cannot predict now',
'It is decidedly so',
'Outlook not so good'
]

shaketime = None
while True:

    x, y, z = sh.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        shaketime = time.time()
    else:
        # If the Sense HAT is still and it's been at least a second
        # since it was last shaken, display the message.
        if shaketime and time.time() - shaketime > 1:
            sh.show_message(random.choice(replies))
            shaketime = None
