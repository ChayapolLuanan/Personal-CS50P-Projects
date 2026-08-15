"""""""""""""""""""""""""""""""""""""""""""""""""""
def main():
    time = input("What time is it? ")
    hour = convert(time)

    if 7 <= hour <= 8:
        print("Breakfast Time")
    elif 12 <= hour <= 13:
        print("Lunch Time")
    elif 18 <= hour <= 19:
        print("Dinner Time")


def convert(time):
    hours, minutes = time.split(" ")
    hours = int(hours)
    minutes = int(minutes)/60
    hours = float(hours + minutes)
    return hours


if __name__ == "__main__":
    main()

---------------------------------------

def main():
    time = input("What time is it? ")
    hours = convert(time)

    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")


def convert(hours, minutes):
    hours, minutes = time.split(" ") #type: ignore
    hours = int(hours)
    minutes = int(minutes)/60
    converted_time = float(hours + minutes)
    return converted_time


if __name__ == "__main__":
    main()
"""""""""""""""""""""""""""""""""""""""""""""""""""

def main():
    time = input("What time is it? ")
    hour = convert(time)

    if 7.0 <= hour <= 8.0:
        print("breakfast time")
    if 12.0 <= hour <= 13.0:
        print("lunch time")
    if 18.0 <= hour <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    return hours + minutes


if __name__ == "__main__":
    main()
