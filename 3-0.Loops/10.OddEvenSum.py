n = int(input())
sumEven = 0
sumOdd = 0

for x in range(1,n+1):
    num = int(input())
    if x % 2 == 0:
        sumEven += num
    else:
        sumOdd += num
if sumEven == sumOdd:
    print(f"Yes\nSum = {sumEven}")
elif sumEven > sumOdd:
    print(f"No\nDiff = {sumEven-sumOdd}")
else:
    print(f"No\nDiff = {sumOdd-sumEven}")