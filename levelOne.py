import random

computer = random.randint(1,10)
guess = 0

while guess < 3:
    player = int(input("Guess a number between 1-10"))

    if player == computer:
        print("You Win!")
        break

    elif player > computer:
        print("Too High")
        guess += 1
        continue

    else:
        print("Too Low")
        guess += 1
        continue

print("You ran out of guesses.")


