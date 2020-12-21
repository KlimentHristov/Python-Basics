import sys
n = int(input())

maxN = -sys.maxsize
minN = sys.maxsize

for x in range(n):
    num = int(input())
    if num < minN:
        minN = num
    if num > maxN:
        maxN = num

print(f"Max number: {maxN}")
print(f"Min number: {minN}")