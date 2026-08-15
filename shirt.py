import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith((".png", ".jpeg", ".jpg")) and not sys.argv[2].endswith((".png", ".jpeg", ".jpg")):
        sys.exit("Invalid input and output")
    elif not sys.argv[1].endswith((".png", ".jpeg", ".jpg")):
        sys.exit("Invalid input")
    elif not sys.argv[2].endswith((".png", ".jpeg", ".jpg")):
        sys.exit("Invalid output")

    valid_ext = (".png", ".jpeg", ".jpg")

main()
