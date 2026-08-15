import requests
import sys
import json


def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoin = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=6be5dd535dbfa10057e07decb12222a876462a37d718816a6a97ede0650c9477"
        )
        bitcoin_json = bitcoin.json()
        bitcoin_price = float(bitcoin_json["data"]["priceUsd"])
        bitcoin_price = float(bitcoin_price) * float(sys.argv[1])

        print(f"${bitcoin_price:,.4f}")

    except requests.RequestException:
        pass
    except ValueError:
        sys.exit("Command-line argument is not a number")


main()
