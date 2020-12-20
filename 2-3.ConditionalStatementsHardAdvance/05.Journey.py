budget = float(input())
season = input()

if budget <= 100:
    if season == "summer":
        budget *= 0.3
    elif season == "winter":
        budget *= 0.7
elif budget > 100 and budget <= 1000:
    if season == "summer":
        budget *= 0.4
    elif season == "winter":
        budget *= 0.8
elif budget > 1000:
    budget *= 0.9

if season == "summer" and budget > 100 and budget <= 1000:
    print(f'Somewhere in Balkans\nCamp - {budget:.2f}')
elif season == "winter" and budget > 100 and budget <= 1000:
    print(f'Somewhere in Balkans\nHotel - {budget:.2f}')

elif season == "summer" and budget <= 100:
    print(f'Somewhere in Bulgaria\nCamp - {budget:.2f}')
elif season == "winter" and budget <= 100:
    print(f'Somewhere in Bulgaria\nHotel - {budget:.2f}')

if (season == "summer" or season == "winter") and budget > 1000:
    print(f'Somewhere in Europe\nHotel - {budget:.2f}')
