def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    numbers = ip.split(".")

    if ip.count(".") != 3:
        return False
    if len(numbers) != 4:
        return False

    for number in numbers:
        if not number:
            return False
        if not number.isdigit():
            return False
        if len(number) > 1 and number[0] == '0':
            return False

        n = int(number)
        if n < 0 or n > 255:
            return False

    return True

if __name__ == "__main__":
    main()
