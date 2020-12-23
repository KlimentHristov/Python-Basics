import sys
import math
n = int(input())
count = 0
countP1 = 0
countP2 = 0
countP3 = 0
countP4 = 0
countP5 = 0

if n > 0 and n <= 1000:
    for i in range(1,n+1):
        num = int(input())
        count += 1
        if num < 200:
            countP1 +=1
        elif num >= 200 and num <= 399:
            countP2 +=1
        elif num >= 400 and num <= 599:
            countP3 +=1
        elif num >= 600 and num <= 799:
            countP4 +=1
        elif num >= 800:
            countP5 +=1
percentP1 = (countP1 / count) * 100
percentP2 = (countP2 / count) * 100
percentP3 = (countP3 / count) * 100
percentP4 = (countP4 / count) * 100
percentP5 = (countP5 / count) * 100

print(f"{percentP1:.2f}%\n{percentP2:.2f}%\n{percentP3:.2f}%\n{percentP4:.2f}%\n{percentP5:.2f}%")