def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    user_input = user_input.strip().lower().replace("-", "")
    words = user_input.split()
    user_input = " ".join(words)

    if user_input == "42" or user_input == "forty two" or user_input == "fortytwo":
        print("Yes")
    else:
        print("No")

main()
