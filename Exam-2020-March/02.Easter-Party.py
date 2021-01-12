guesses = int(input())
price_per_person = float(input())
budget = float(input())
discount = 0

crem = float((budget * 10) / 100)

if 10 <= guesses <= 15:
    discount = price_per_person - (price_per_person * 15) / 100
elif 15 < guesses <= 20:
    discount = price_per_person - (price_per_person * 20) / 100
elif guesses > 20:
    discount = price_per_person - (price_per_person * 25) / 100
else:
    discount = price_per_person
all_sum = crem + (guesses * discount)

if all_sum > budget:
    print(f"No party! {(all_sum - budget):.2f} leva needed.")
else:
    print(f"It is party time! {(budget - all_sum):.2f} leva left.")
