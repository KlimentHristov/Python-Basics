n = int(input())
multi = 1

for i in range(n):
    if multi >= i:
        print(multi)
        multi = (multi * 2)+1
    if multi > n:
        break



