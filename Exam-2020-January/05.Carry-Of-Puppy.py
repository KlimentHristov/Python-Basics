kilograms = float(input()) * 1000
sum = 0
magicWord = ""

while magicWord != "Adopted":
    currentGram = input()
    if currentGram == "Adopted":
        break
    else:
        currentGram = float(currentGram)
    sum += float(currentGram)

if sum <= kilograms:
    print(f"Food is enough! Leftovers: {float(kilograms-sum):.0f} grams.")
else:
    print(f"Food is not enough. You need {float(sum - kilograms):.0f} grams more.")
