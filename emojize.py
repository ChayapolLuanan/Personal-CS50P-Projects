import emoji

def main():
    emoji_inputted = input("Input: ")
    print(emoji.emojize(f"{emoji_inputted}", language="alias"))


main()

