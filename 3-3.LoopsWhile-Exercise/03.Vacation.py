vacation = float(input())
money = float(input())

spendDays = 0
counterDays = 0

while money < vacation and spendDays < 5:
    action = input()
    currentSum = float(input())
    counterDays += 1
    if action == "save":
        money += currentSum
        spendDays = 0
    if action == "spend":
        spendDays += 1
        if currentSum > money:
            money = 0
        else:
            money -= currentSum
if money >= vacation:
    print(f"You saved the money for {counterDays} days.")
if spendDays == 5:
    print(f"You can\'t save the money.\n{counterDays}")
