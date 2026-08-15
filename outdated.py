def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]


    while True:
        user_input = input("Date: ").strip()

        if "/" in user_input:
            system_parts = user_input.split("/")
            if len(system_parts) == 3:
                month = int(system_parts[0])
                date = int(system_parts[1])
                year = int(system_parts[2])
                if 1 <= month <= 12 and 1 <= date <= 31:
                    print(f"{year:04d}-{month:02d}-{date:02d}")
                    break

        elif "," in user_input:
            try:
                words = user_input.split(" ")
                month = words[0]
                date = int(words[1].replace(",", ""))
                year = int(words[2])
                if month in months and 1 <= date <= 31:
                    month = months.index(month) + 1
                    print(f"{year:04d}-{month:02d}-{date:02d}")
                    break
            except:
                pass

        print("Invalid date. Please try again.")

main()
