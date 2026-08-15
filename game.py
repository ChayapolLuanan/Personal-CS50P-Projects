import random
import sys

def main():

    while True:
        try:
            level = int(input("Level: ").strip())
            answer = random.randint(1, level)
            break
        except ValueError:
            pass

    while True:
        try:
            guess = int(input("Guess: ").strip())

            if guess < answer:
                print("Too small!")
            elif guess > answer:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()


        except ValueError:
            pass

main()
