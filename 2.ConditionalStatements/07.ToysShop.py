puzzle = 2.60
dolls = 3
teddybear = 4.10
minion = 8.20
truck = 2

priceTravell = float(input())

# declare number of tools
countPuzzle = float(input())
countDolls = float(input())
countTeddyBear = float(input())
countMinion = float(input())
countTruck = float(input())
allCount = countPuzzle + countDolls + countTeddyBear + countMinion + countTruck

# calculation price of tools
pricePuzzle = countPuzzle * puzzle
priceDolls = countDolls * dolls
priceTeddy = countTeddyBear * teddybear
priceMinion = countMinion * minion
priceTruck = countTruck * truck
allPrice = pricePuzzle + priceDolls + priceTeddy + priceMinion + priceTruck

discount = 0

if allCount >= 50:
    discount = allPrice * 0.25

finalPrice = allPrice - discount
rent = finalPrice * 0.1
gain = finalPrice - rent

if gain > priceTravell:
    gain = gain - priceTravell
    print(f"Yes! {gain:.2f} lv left")
elif gain < priceTravell:
    gain = priceTravell - gain
    print(f"Not enough money! {gain:.2f} lv needed")
