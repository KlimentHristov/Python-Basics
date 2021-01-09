wall = '|'
empty = " "
star = "*"
row =0

n = int(input())

#start
print(f"{(n-row+1)*empty}{wall}{(n-row+1)*empty}")

#middle
for row in range(1,n+1):
    print(f"{(n-row)*empty}{row * star} {wall} {(row-n)*empty}{row * star}")


