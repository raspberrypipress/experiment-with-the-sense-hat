import random
import time

print("Ask a question?")

time.sleep(3)

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

print(random.choice(replies))