days = float(input())
countSweets = float(input())

countCakes = float(input())
countCrimps = float(input())
countPep= float(input())

priceCakes = countCakes * 45
priceCrimps = countCrimps * 5.80
pricePep = countPep * 3.20
# calculations for day
oneDay = (priceCakes + priceCrimps + pricePep) * countSweets
# all sum for campagne
allSum = oneDay * days
# expenses
allPrice = allSum - (allSum / 8)

print(f'{allPrice:.2f}')