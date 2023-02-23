import random

player = int(input("Pick a number between 1 and 10"))
guess = 0

while guess < 3:
    computer = random.randint(1, 10)
    print(f'CPU Picked {computer}')

    if computer == player:
        print("CPU Wins")
        guess += 1
        break

    elif computer > player:
        print("CPU Guessed Too High")
        guess += 1

    else:
        print("CPU Guessed to Low")
        guess += 1

if guess == 3:
    print('CPU lost')