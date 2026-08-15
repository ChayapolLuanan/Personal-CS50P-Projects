import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        total_lines = 0
        with open(filename, "r") as f:
            for line in f:
                stripped_lines = line.lstrip()  #removes black spaces
                if stripped_lines and not stripped_lines.startswith("#"):    #removes the comment line
                    total_lines += 1    #adds 1 to total_lines for every one of these lines
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(total_lines)

main()
