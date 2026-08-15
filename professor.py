import random


def main():

    level = get_level()
    correct_answers = 0


    for _ in range(10):

        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0


        while True:

            print(f"{x} + {y} = ", end="")
            user_answer = int(input("").strip())

            if user_answer == (x + y):
                correct_answers = correct_answers + 1
                break
            else:
                tries = tries + 1
                print("EEE")
                try:
                    if tries == 3:
                        print(f"{x} + {y} = {x + y}")
                        break
                    else:
                        pass
                except ValueError:
                    pass


    print(f"Score: {correct_answers}")




def get_level():
    while True:
        try:
            user_input = int(input("Level: ").strip())
            if 1 <= user_input <= 3:
                return user_input
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)



if __name__ == "__main__":
    main()
