sum = 0
random = input()

while random != "NoMoreMoney":
    num = float(random)
    if num <= 0:
        print(f"Invalid operation!")
        break
    sum += num
    print(f"Increase: {num:.2f}")
    random = input()
print(f"Total: {sum:.2f}")

