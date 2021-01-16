fruit = input()
size = input()
countSets = float(input())
discount = 0

smallPack = 2
bigPack = 5

if fruit == "Watermelon":
    if size == "small":
        smallPack *= 56
        countSets *= smallPack
    elif size == "big":
        bigPack *= 28.70
        countSets *= bigPack
elif fruit == "Mango":
    if size == "small":
        smallPack *= 36.66
        countSets *= smallPack
    elif size == "big":
        bigPack *= 19.60
        countSets *= bigPack
elif fruit == "Pineapple":
    if size == "small":
        smallPack *= 42.10
        countSets *= smallPack
    elif size == "big":
        bigPack *= 24.80
        countSets *= bigPack
elif fruit == "Raspberry":
    if size == "small":
        smallPack *= 20
        countSets *= smallPack
    elif size == "big":
        bigPack * 15.20
        countSets *= bigPack

if  countSets >=400 and countSets <= 1000:
    discount = float((countSets * 15)/100)
elif countSets > 1000:
    discount = float((countSets * 50)/100)

print(f"{(countSets -discount):.2f} lv.")

