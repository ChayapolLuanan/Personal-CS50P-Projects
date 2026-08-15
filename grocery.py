def main():
    list = {}

    try:
        while True:
            something = input().upper().strip()
            if something:
                if something in list:
                    list[something] += 1
                if not(something in list):
                    list[something] = 1
    except EOFError:
        pass
    for something in sorted(list):
        print(f"{list[something]} {something}")

main()
