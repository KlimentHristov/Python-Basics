kozunaci = float(input()) * 3.20
kori = int(input())
kurabii = int(input()) * 5.40
boya = float(kori*12*0.15)
priceEggs = kori * 4.35
sum = kozunaci + priceEggs + kurabii + boya
print(f"{sum:.2f}")
