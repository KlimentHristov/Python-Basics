randomNum = int(input())
randomNumCheck = randomNum
bonus = 0

if randomNum <= 100:
    randomNum += 5
    bonus += 5
elif randomNum > 100 and randomNum < 1000:
    randomNum = randomNum + (randomNum * 0.2)
    bonus = randomNumCheck * 0.2
elif randomNum >= 1000:
    randomNum = randomNum + (randomNum * 0.1)
    bonus = randomNumCheck * 0.1
if randomNumCheck % 2 == 0:
    randomNum += 1
    bonus += 1
elif randomNumCheck % 10 == 5:
    randomNum += 2
    bonus += 2

print(bonus)
print(randomNum)
