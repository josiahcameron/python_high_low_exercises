import random

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



def play():
    player_number = int(input('Pick a number between 1 and 10'))
    min_num, max_num = 1, 10
    counter = 0

    while True:
        computer_number = (min_num + max_num) // 2
        counter +=1

        if compuer_number == player_number:
            print(f"The computer guessed your number is {counter} tries.")
            break

        if computer > player:
            print("CPU Guessed too Low")
            guess += 1
            min_num = computer + 1

        if computer < player:
            print("CPU Guessed too High")
            guess -= 1
            max_num = computer - 1
        

if __name__=='__main__':
    play()