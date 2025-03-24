import random
guess_number=random.randint(1,100)
while True:
        user=int(input("guess the number FROM 1 TO 100:"))

        if user<guess_number:
            print("too low!")
        elif user>guess_number:
            print("too high")
        else:
            print("congrats,you guessed the number")
            break

