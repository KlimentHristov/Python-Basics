bitcoin = float(input()) * 1168
chinaYena = float(input()) * 0.15
commision = float(input())

usd = 1.76
euro = 1.95

chinaYena = float(chinaYena*usd) # lv
sum = bitcoin + chinaYena
sumEUR =  float(sum/euro)

commision = float((sumEUR * commision)/100)
sumEUR -=commision

print(f"{sumEUR:.2f}")







