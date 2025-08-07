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
    try:
        prompt = input("Date: ")
        month, day, year = prompt.split('/')      
        month = int(month)
        day = int(day)

        if month > 12:
            continue

        else:
            print(f"{year}-{month:02}-{day:02}")

        break
    except ValueError:
        try:
            item, year = prompt.split(", ")
            month, day = item.split(" ")
            day = int(day)

            if day > 31:
                continue

            elif month in months:
                print(f"{year}-{months.index(month) + 1:02}-{day:02}")
                
                break
        except ValueError:
            pass
