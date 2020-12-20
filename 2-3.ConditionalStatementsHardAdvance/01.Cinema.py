type = input()
rows = int(input())
columns = int(input())

allPlaces = rows * columns

if type == "Premiere":
    allPlaces *= 12
elif type =="Normal":
    allPlaces *= 7.50
elif type == "Discount":
    allPlaces *= 5

print(f"{allPlaces:.2f} leva")