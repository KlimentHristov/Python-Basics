city = input()
sales = float(input())
price = 0

if city == "Sofia":
    if sales >= 0 and sales <= 500:
        price = sales * 0.05
    if sales > 500 and sales <= 1000:
        price = sales * 0.07
    if sales > 1000 and sales <= 10000:
        price = sales * 0.08
    if sales > 10000:
        price = sales * 0.12
elif city == "Varna":
    if sales >= 0 and sales <= 500:
        price = sales * 0.045
    if sales > 500 and sales <= 1000:
        price = sales * 0.075
    if sales > 1000 and sales <= 10000:
        price = sales * 0.10
    if sales > 10000:
        price = sales * 0.13
elif city == "Plovdiv":
    if sales >= 0 and sales <= 500:
        price = sales * 0.055
    if sales > 500 and sales <= 1000:
        price = sales * 0.08
    if sales > 1000 and sales <= 10000:
        price = sales * 0.12
    if sales > 10000:
        price = sales * 0.145

if sales < 0 or city != "Sofia" and city != "Varna" and city != "Plovdiv":
    print("error")
else:
    print(f"{price:.2f}")

