# CSV Binary Encoder and Decoder

#### Video Demonstration Link: https://youtu.be/el2H5Eg_v84?si=7EocuDVxic5c6XlO

#### Project Description:
For the CS50P final project, I have decided to create a binary encoder and decoder controlled through the command-line interface. It is designed to
convert text data within a given CSV file to and from 8-bit binary representation. It analyses structured tabular data by either encoding or decoding
string values in each cell without losing the header information of the CSV file. In this way, a user is able to easily hide data or decode original messages from the
dataset without breaking the tabular nature of the file.

### File Structures and Features:

#### project.py
## main() function in project.py:
This is the main function that controls the main parts of the application. The function checks for whether the user passed exactly three arguments: input file, output file,
and the mode. It also verifies the execution mode (either "encode" or "decode"). It triggers the CSV processing pipeline. If the user input is invalid, it will terminate
the program safely and prompt the user with clear instructions.

## text_to_binary() function in project.py:
This function takes a text string and translates its string of 8-bit binary codes. It represents every character in 8-bit binary code using Python's built-in
"ord()" function separated by spaces using the ord() function. Lastly, it adds white spaces between characters, so that it is clear which set of 8 bits are which letter.

## binary_to_text() function in project.py:
It first splits an ASCII binary string by spaces into 8-bit chunks. Then, it goes through each one of them and checks for only "0" and "1" characters. After the validation,
it converts the base-2 number to an ASCII character using the "chr()" and "int(chunk, 2)". Lastly, it returns the reconstructed text string and raises ValueError for
invalid segments.

## process_csv() function in project.py:
This function opens the CSV file using "csv.DictReader", processes all columns of all rows and uses the appropriate helper function. The "process_csv" function takes care
of all errors in cells and writes all results to a new CSV file using "csv.DictWriter".

#### test_project.py:
Contains teh automated testing framework using "pytest". The framework is used to verify my customized helper functions, which are text_to_binary, binary_to_text, and
process_csv. The tests check both correct and incorrect usage of those functions (file not found, wrong argument, corrupted chunk, and etc.).

### Design Choices and Challenges
A few design choices were made during the process of developing this project in order to maek sure that it is working properly and face as little amount of problems
as possible. Firstly, instead of the usage of text file reading, I used the functions (csv.DictReader and csv.DictWriter)in the external libraries that I have imported
at the very start of my program (csv). This module is capable of automatically handling headers and manipulating tabular data via structure as input.

Secondly, instead of asking the user about the input/output file or typing -help for help (via input()), I have decided to use command-line arguments (sys.argv) and
make my program execute fast and easily integrating into automation scripts.

However, not everything was smooth throughout the process of coding this program–causing me to face a few challenges. The most challenging part of this project was
when I encountered a very small problem, but it had a significant impact on my overall code. This problem was in terms of syntax error because I had put 2 lines in
a small loop when it should've been in a big loop in my binary_to_text function. This caused my output file to repeat the letters 8 times like
"HHHHHHHHeeeeeeeelllllllloooooooo", instead of "Hello".

### Usage:
Type in the interface the input file that has the text that needs encoding/decoding, the desired output file, and the mode (either encode/decode)

```bash
python project.py sample.csv output.csv encode
