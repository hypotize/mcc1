#python3 -m pip install getkey
from getkey import getkey, keys
import time
import random

num = random.randint(5,10)

start  = time.time()
print ("Hit enter after", num, "seconds")

key1 = getkey()
elapsed1 = round(time.time() - start, 2)

key2 = getkey()
elapsed2 = round(time.time() - start, 2)

print("Key", key1, "time was", elapsed1, "seconds")
print("Key", key2, "time was", elapsed2, "seconds")

diff1 = abs(num - elapsed1)
diff2 = abs(num - elapsed2)

if diff1 == diff2:
    print("draw")
elif diff1 < diff2:
    print(key1, "wins")
else:
    print(key2, "wins")
