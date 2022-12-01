import time
import random

num = random.randint(5,10)

print ("Hit enter after", num, "seconds")

start  = time.time()
input()
now = time.time()
elapsed = int(now - start)

if elapsed == num :
    print("Perfect! That was", num, "seconds")
else:
    print("Close! You were aiming for", num, "seconds but got", elapsed, "secon\
ds")
