n = int(input())

leftSum = 0
rightSum = 0

for x in range(n):
    random1 = int(input())
    leftSum += random1
for y in range(n):
    random2 = int(input())
    rightSum += random2

if leftSum == rightSum:
    print(f"Yes, sum = {leftSum}")
else:
    print(f"No, diff = {abs(leftSum-rightSum)}")
