years = int(input())
price = float(input())
priceForToys = float(input())
count = 0
toys = 0
secondBD = 0
brother = 0
increase = 10
if years > 0 <= 77:
    for i in range(1,years+1):
        if i % 2 == 0:
            count += secondBD
            secondBD += 10
            brother +=1
        else:
            toys +=1

priceForToys *= toys
allPrice = (priceForToys + secondBD + count) - brother

if allPrice >= price:
    final = allPrice - price
    print(f"Yes! {final:.2f}")
elif allPrice < price:
    final = price - allPrice
    print(f"No! {final:.2f}")

