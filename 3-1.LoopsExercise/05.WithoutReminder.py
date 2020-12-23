import sys
import math
n = int(input())
count = 0
countP2 = 0
countP3 = 0
countP4 = 0

if n > 0 and n <= 1000:
    for i in range(1,n+1):
        num = int(input())
        count += 1
        if num % 2 == 0:
            countP2 +=1
            if num % 3 == 0:
                countP3 += 1
            if num % 4 == 0:
                countP4 += 1
        elif num % 3 == 0:
            countP3 += 1
            if num % 2 == 0:
                countP2 += 1
            if num % 4 == 0:
                countP4 += 1

        elif num % 4 == 0:
            countP4 +=1
            if num % 2 == 0:
                countP2 += 1
            if num % 3 == 0:
                countP3 += 1

percentP2 = (countP2 / count) * 100
percentP3 = (countP3 / count) * 100
percentP4 = (countP4 / count) * 100

print(f"{percentP2:.2f}%\n{percentP3:.2f}%\n{percentP4:.2f}%")