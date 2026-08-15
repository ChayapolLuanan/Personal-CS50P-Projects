def main():
    guest_input = input("Expression: ")

    x, y, z = guest_input.split(" ")
    x = float(x)
    z = float(z)

    if y == "*":
        answer = x * z
    elif y == "+":
        answer = x + z
    elif y == "-":
        answer = x - z
    elif y == "/":
        answer = x / z
    else:
        print("Please enter a valid expression")

    print(f"{answer:.1f}")

main()
