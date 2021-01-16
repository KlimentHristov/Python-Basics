destination = input()
dates = input()
nights = int(input())

if destination == "France":
    if dates == "21-23":
        nights *= 30
    elif dates == "24-27":
        nights *= 35
    elif dates == "28-31":
        nights *= 40
elif destination == "Italy":
    if dates == "21-23":
        nights *= 28
    elif dates == "24-27":
        nights *= 32
    elif dates == "28-31":
        nights *= 39
elif destination == "Germany":
    if dates == "21-23":
        nights *= 32
    elif dates == "24-27":
        nights *= 37
    elif dates == "28-31":
        nights *= 43
print(f"Easter trip to {destination} : {nights:.2f} leva.")