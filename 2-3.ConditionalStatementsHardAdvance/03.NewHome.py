typeFlowers = input()
count = int(input())
budget = int(input())
price = 0

if typeFlowers == "Roses":
    price = count * 5
    if count > 80:
        price = price - (price * 0.1)
elif typeFlowers == "Dahlias":
    price = count * 3.80
    if count > 90:
        price = price - (price * 0.15)
elif typeFlowers == "Tulips":
    price = count * 2.80
    if count > 80:
        price = price - (price * 0.15)
elif typeFlowers == "Narcissus":
    price = count * 3
    if count < 120:
        price = price + (price * 0.15)
elif typeFlowers == "Gladiolus":
    price = count * 2.50
    if count < 80:
        price = price + (price * 0.20)

if budget >= price:
    budget -= price
    print(f"Hey, you have a great garden with {count} {typeFlowers} and {budget:.2f} leva left.")
elif budget < price:
    price -= budget
    print(f'Not enough money, you need {price:.2f} leva more.')
