def main():
    user_input = input("Input: ").strip()
    shorten_word = shorten(user_input)
    print(shorten_word)


def shorten(user_input):
    twttr_sentence = []

    for letter in user_input:
        match letter.lower():
            case "a", "e", "i", "o", "u":
                pass
            case _:
                twttr_sentence.append(letter)

    shorten_word = "".join(shorten_word)
    return(shorten_word)


if __name__ == "__main__":
    main()
