import random

num = random.randint(1,100)

print ("guess the number")

guess = int(input())
count = 1

while guess != num:
    if guess < num:
        print ("guess higher")
    else:
        print("guess lower")
        print ("guess the number again")

    guess = int(input())
    count += 1

print ("the number was", num, " and it took you ", count, " tries to get it")

