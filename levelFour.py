import random




while True:
    choice = input("Pick A Level \nLevel A: \nLevel B: \nLevel C: \n").lower()
    
    if choice == "a":

        print("In level one, the computer generates a random number between 1 and 10 and the user has 3 guesses to pick the correct number. The computer will tell you if you are too high or too low.")
        computer = random.randint(1,10)
        guess = 0

        while guess < 3:
            player = int(input("Guess a number between 1-10: "))

            if player == computer:
                print("You Win!")
                break

            if player > computer:
                print("Too High")
                guess += 1
                continue

            else:
                print("Too Low")
                guess += 1
                continue

        if guess > 3:
            print("You ran out of guesses.")
        break
        

    elif choice == 'b':
        print("In level two, the game is reversed and the user picks a number and the computer then has 3 guesses to select the correct answer.")
        player = int(input("Pick a number between 1 and 10: "))
        guess = 0

        while guess < 3:
            computer = random.randint(1, 10)
            print(f'CPU Picked {computer}')

            if computer == player:
                print("CPU Wins")
                guess += 1

            elif computer > player:
                print("CPU Guessed Too High")
                guess += 1

            else:
                print("CPU Guessed too Low")
                guess += 1
        print('CPU loses!')
        break

    elif choice == 'c':
        print("In level three, the computer's guesses are optimized to refine the range on the guesses based on whether they are too high or too low.")
        player = int(input("Pick a number between 1 and 10: "))
        guess = 0
        min = 1
        max = 10

        computer = random.randint(1, 10)
        print(f"CPU Guessed {computer}")

        while computer is not player:

            if computer > player:
                print("CPU Guessed Too High")
                guess += 1
                max = computer - 1
                computer = random.randint(min, max)
                print(f'CPU Picked {computer}')
                continue

            else:
                print("CPU Guessed to Low")
                guess += 1
                min = computer + 1
                computer = random.randint(min, max)
                print(f'CPU Picked {computer}')
                continue
        print(f"It Took CPU {guess} Times To Figure It Out")
        break

    else:
        print("Your choice is outside the given parameters")
        continue

