month = input()
countNights = float(input())

studio = 0
apart = 0

if month == "May" or month == "October":
    studio = countNights * 50
    apart = countNights * 65
elif month == "June" or month == "September":
    studio = countNights * 75.20
    apart = countNights * 68.70
elif month == "July" or month == "August":
    studio = countNights * 76
    apart = countNights * 77

if countNights > 14:
    apart *= 0.9
    if month == "June" or month == "September":
        studio *= 0.80
    elif month == "May" or month == "October":
        studio *= 0.70
elif countNights > 7 and countNights < 14:
    studio *= 0.95

print(f"Apartment: {apart:.2f} lv.\nStudio: {studio:.2f} lv.")