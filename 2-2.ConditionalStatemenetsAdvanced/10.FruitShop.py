product = input()
day = input()
quantity = float(input())
price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if product == "banana":
        price = 2.50
    if product == "apple":
        price = 1.20
    if product == "orange":
        price = 0.85
    if product == "grapefruit":
        price = 1.45
    if product == "kiwi":
        price = 2.70
    if product == "pineapple":
        price = 5.50
    if product == "grapes":
        price = 3.85
elif day == "Saturday" or day == "Sunday":
    if product == "banana":
        price = 2.70
    if product == "apple":
        price = 1.25
    if product == "orange":
        price = 0.90
    if product == "grapefruit":
        price = 1.60
    if product == "kiwi":
        price = 3.00
    if product == "pineapple":
        price = 5.60
    if product == "grapes":
        price = 4.20
allPrice = price*quantity
if day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday" and day != "Saturday" and day != "Sunday":
    print("error")
elif product != "banana" and product != "apple" and product != "orange" and product != "grapefruit" and product != "kiwi" and product != "pineapple" and product != "grapes":
    print("error")
else:
    print(f"{allPrice:.2f}")
