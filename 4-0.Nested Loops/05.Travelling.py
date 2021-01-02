destination = input()

while destination != "End":
    budget = float(input())
    needMoney = 0
    while budget > needMoney:
        currentMoney = float(input())
        needMoney += currentMoney
    print(f"Going to {destination}!")
    destination = input()





