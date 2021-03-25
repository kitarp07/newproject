import random

num = random.randint(1,30)

while True:
    guess = int(input("please guess the number: "))
    if guess==num:
        print('right')
