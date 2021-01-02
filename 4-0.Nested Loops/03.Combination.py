n = int(input())
counter = 0

for i in range(0,n+1):
    for j in range(0,n+1):
        for y in range(0,n+1):
            if i + j + y == n:
                counter+=1
print(counter)

