budget = float(input())
decor = budget * 0.1
statists = float(input())
priceStatist = float(input())
priceStatist = priceStatist * statists

if statists > 150:
    priceStatist -= (priceStatist * 0.1)
allPrice = decor + priceStatist
if allPrice > budget:
    allPrice -= budget
    print(f"Not enough money!\nWingard needs {allPrice:.2f} leva more.")
elif allPrice <= budget:
    budget -= allPrice
    print(f"Action!\nWingard starts filming with {budget:.2f} leva left.")


