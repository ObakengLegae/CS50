
while True:
    try:
        prompt = (input("fraction: "))
        x,y = prompt.split("/") 
        x = int(x)
        y = int(y)
        if x > y:
            continue         
        z = int(x)/int(y)
        if z < 0:
            continue       
        percentage = z * 100
        if 0 <= percentage <= 1:
            print("E")
        elif percentage > 98:
            print("F")
        else:
            print(f'{round(percentage)}%')

        break

    except (ValueError, ZeroDivisionError):
        pass        

