def main():
    time = input("What time is it (24-hour time)? ")
    meal_time = convert(time)
    if 7 <= meal_time <=8 :
        print("breakfast time")
    elif 12 <= meal_time <= 13:
        print("lunch time")
    elif 18 <= meal_time <= 19:
        print("dinner time")
    else:
        print()


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = float(minutes) / 60
    return hours + minutes


if __name__ == "__main__":
    main()
