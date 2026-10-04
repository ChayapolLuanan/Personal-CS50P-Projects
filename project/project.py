import sys
import csv

def main():
    if len(sys.argv) != 4:
        print("Error. Please check your input!")
        print(
            "Usage: python project.py <input_file> <output_file> <encode/decode>\n"
            "input_file must exist and must be a CSV file \n"
            "output_file is the destination file \n"
            "mode must either be encode or decode"
        )
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    mode = sys.argv[3].strip().lower()

    if mode != "encode" and mode != "decode":
        sys.exit("Error: Mode must be either 'encode' or 'decode'.")

    process_csv(input_file, output_file, mode)

def text_to_binary(text):
    if not text:
        return ""

    binary_list = []
    for char in text:
        binary_char = f"{ord(char):08b}"
        binary_list.append(binary_char)

    return " ".join(binary_list)

def binary_to_text(binary_str):
    binary_str = binary_str.strip()
    if not binary_str:
        return ""

    chunks = binary_str.split(" ")
    decoded_chars = []

    for chunk in chunks:
        if len(chunk)!= 8:
            raise ValueError(f"Chunk '{chunk}' is not 8 bits long")

        for bit in chunk:
            if bit != "0" and bit != "1":
                raise ValueError(f"Invalid binary character '{bit}' in chunk '{chunk}'")

        char_code = int(chunk, 2)
        decoded_chars.append(chr(char_code))

    return "".join(decoded_chars)

def process_csv(input_path, output_path, mode):
    try:
        with open(input_path, "r", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames

            if not fieldnames:
                sys.exit("Error: CSV file is empty or missing headers")

            rows = []
            line_num = 2
            for row in reader:
                new_row = {}
                for col_name, value in row.items():
                    if value is None:
                        new_row[col_name] = ""
                        continue
                    try:
                        if mode == "encode":
                            new_row[col_name] = text_to_binary(value)
                        elif mode == "decode":
                            new_row[col_name] = binary_to_text(value)
                    except ValueError as error:
                        print(f"Warning on line {line_num}, column '{col_name}': {error}")
                        new_row[col_name] = "[CORRUPTED]"

                rows.append(new_row)
                line_num += 1

        with open(output_path, "w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"Finished processing! Saved result to {output_path}")

    except FileNotFoundError:
        sys.exit(f"Error: File '{input_path}' could not be found")

if __name__ == "__main__":
    main()
