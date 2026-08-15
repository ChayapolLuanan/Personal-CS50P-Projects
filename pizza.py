import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too less command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        filename = sys.argv[1]
        with open(filename) as f:
            read = csv.reader(f)
            print(tabulate(read, headers = "firstrow", tablefmt = "grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

main()
