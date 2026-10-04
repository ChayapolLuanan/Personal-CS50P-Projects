from datetime import date
import sys

def main():
    print(find_minutes(input("Date of Birth: ")))

def find_minutes(s):
    try:
        year, month, day = s.split("-")
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            sys.exit(1)
        if not len(year) == 4:
            sys.exit(1)

        birth_date = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit(1)

    today_date = date.today()
    total_dates = (today_date - birth_date).days
    total_minutes_aged = total_dates * 24 * 60

    return f"{numbers_to_words(total_minutes_aged)} minutes"

def numbers_to_words(n):
    one_digits_C = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    one_digits_LC = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ten_to_twenty = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    increases_by_ten = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million"]

    def convert_section(numbers):
        total_minutes_in_num = []
        if numbers >= 100:
            # This needs to be one_digits_C (or the capatilized version of one_digits) because it is the 1st word in the final result
            total_minutes_in_num.append(one_digits_C[numbers // 100] + " hundred")
            numbers %= 100 #finds the remainder of when the numbers is divided by 100
        if 10 <= numbers < 20:
            # if numbers = 11, 11-10=1 which means that ten_to_twenty[1] (which is Eleven (which is the same as numbers))
            total_minutes_in_num.append(ten_to_twenty[numbers - 10])
        else:
            if numbers >= 20:
                t = increases_by_ten[numbers // 10]
                o = one_digits_LC[numbers % 10]
                total_minutes_in_num.append(f"{t}-{o}" if o else t)
            elif numbers > 0:
                total_minutes_in_num.append(one_digits_LC[numbers])
        return " ".join(total_minutes_in_num)

    output = []
    section_i = 0

    while n > 0:
        section = n % 1000
        if section > 0:
            section_in_alpha = convert_section(section)
            if thousands[section_i]:
                section_in_alpha += " " + thousands[section_i]
            output.append(section_in_alpha)
        n //= 1000
        section_i += 1

    result = " ".join(reversed(output))
    return result.capitalize()

if __name__ == "__main__":
    main()
