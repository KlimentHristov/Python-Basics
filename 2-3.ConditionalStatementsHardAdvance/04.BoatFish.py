budget = int(input())
season = input()
count = int(input())

rentShip = 0

if season == "Spring":
    rentShip += 3000
elif season == "Summer" or season == "Autumn":
    rentShip += 4200
elif season == "Winter":
    rentShip += 2600

if count <= 6:
    rentShip = rentShip - (rentShip * 0.1)
elif count > 6 and count <= 11:
    rentShip = rentShip - (rentShip * 0.15)
elif count >= 12:
    rentShip = rentShip - (rentShip * 0.25)

if count % 2 == 0:
    if season == "Autumn":
        rentShip = rentShip + 0
    else:
        rentShip = rentShip - (rentShip * 0.05)

if rentShip <= budget:
    budget -= rentShip
    print(f"Yes! You have {budget:.2f} leva left.")
elif rentShip > budget:
    rentShip -= budget
    print(f"Not enough money! You need {rentShip:.2f} leva.")



