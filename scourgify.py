import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        with open(sys.argv[1], "r") as f_in, open(sys.argv[2], "w", newline="") as f_out:
            reader = csv.DictReader(f_in)
            writer = csv.DictWriter(f_out, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(",")
                writer.writerow(
                    {
                        "first": first.strip(),
                        "last": last.strip(),
                        "house": row["house"],
                    }
                )

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

main()
