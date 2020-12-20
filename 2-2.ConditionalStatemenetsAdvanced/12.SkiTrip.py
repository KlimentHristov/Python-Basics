days = int(input())
room = input()
rate = input()

discount = 0
price = 0
allPrice = 0

if room == "room for one person":
    price = (days-1) * 18
elif room == "apartment":
    price = (days-1) * 25
    if days < 10:
        price = price - (price * 0.3)
    elif days >= 10 and days <= 15:
        price = price - (price * 0.35)
    elif days > 15:
        price = price - (price * 0.5)
elif room == "president apartment":
    price = (days-1) * 35
    if days < 10:
        price = price - (price * 0.1)
    elif days >= 10 and days <= 15:
        price = price - (price * 0.15)
    elif days > 15:
        price = price - (price * 0.2)


if rate == "positive":
    allPrice = price + (price * 0.25)
elif rate == "negative":
    allPrice = price - (price * 0.1)
print(f"{allPrice:.2f}")
