import math

income = float(input())
middleRate = float(input())
minSalary = float(input())

highScolarship = 0
socialScolarship = 0

if middleRate >= 5.50:
    highScolarship = middleRate * 25

if income < minSalary and middleRate > 4.50:
    socialScolarship = minSalary * 0.35

if socialScolarship > highScolarship:
        print(f"You get a Social scholarship {math.floor(socialScolarship)} BGN")
if highScolarship >= socialScolarship:
    if highScolarship != 0:
        print(f"You get a scholarship for excellent results {math.floor(highScolarship)} BGN")
    else:
        print("You cannot get a scholarship!")