import math

squareMeters = float(input())
price = squareMeters * 7.61

discount = (price * 18)/100
finalPrice = price - discount

print(f"The final price is : {finalPrice:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")