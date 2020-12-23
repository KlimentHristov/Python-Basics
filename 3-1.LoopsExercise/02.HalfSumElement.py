import sys

random = int(input())
sum = 0
saveMax = -sys.maxsize

for x in range(0,random):
    n = int(input())
    sum += n
    if n > saveMax:
        saveMax = n
final = sum - saveMax

if saveMax == final:
    print(f"Yes\nSum = {saveMax}")
elif saveMax > final:
    saveMax -= final
    print(f"No\nDiff = {saveMax}")
elif saveMax < final:
    final -= saveMax
    print(f"No\nDiff = {final}")




