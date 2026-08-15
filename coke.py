def main():
    coke_price = 50
    cents_used = 0

    while cents_used < coke_price:
        print(f"Amount Due: {coke_price - cents_used}")
        coin = int(input("Insert coin: "))

        if coin in [5, 10, 25]:
            cents_used += coin
        else:
            print("Invalid coin.")

    change = cents_used - coke_price
    print(f"Change Owed: {change}")

main()
