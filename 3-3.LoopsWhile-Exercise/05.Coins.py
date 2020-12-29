
import math
import math

monets = float(input())
rest = math.floor(monets * 100)
coins = 0

while rest > 0:
    if rest >= 200:
        coins += 1
        rest -= 200
    elif rest >= 100:
        coins +=1
        rest -= 100
    elif rest >= 50:
        coins +=1
        rest -= 50
    elif rest >= 20:
        coins +=1
        rest -= 20
    elif rest >= 10:
        coins +=1
        rest -= 10
    elif rest >= 5:
        coins +=1
        rest -= 5
    elif rest >= 2:
        coins +=1
        rest -= 2
    elif rest >= 1:
        coins +=1
        rest -= 1
print(coins)















