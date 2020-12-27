student = input()
middleCount = 0
countAllRates = 0
sum = 0

for i in range(0,12):
    rate = float(input())
    if rate < 4:
        middleCount +=1
    if middleCount > 1:
        break
    countAllRates +=1
    sum +=rate
middleRate = sum / countAllRates
if middleCount > 1:
    print(f"{student} has been excluded at {countAllRates} grade")
else:
    print(f"{student} graduated. Average grade: {middleRate:.2f}")