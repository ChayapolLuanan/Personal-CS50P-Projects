import sys

from pyfiglet import Figlet
figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        user_input = input("Input: ").strip()

        print("Output:")
        print(figlet.renderText(user_input))

    elif len(sys.argv) == 3:
        try:
            search_list = figlet.getFonts()
            search_list.index(sys.argv[2])
            pass

        except ValueError:
            sys.exit("Invalid usage")

        if sys.argv[1] != "-f":
            sys.exit("Invalid usage")

        figlet.setFont(font=(sys.argv[2]))
        user_input = input("Input: ").strip()

        print("Output:")
        print(figlet.renderText(user_input))
        
    else:
        sys.exit("Invalid usage")

main()
