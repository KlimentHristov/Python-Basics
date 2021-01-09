n = int(input())
minus = "-"
star = "*"
wall = '|'
count = 0
if n % 2 == 0:
    count = 2
else:
    count = 1

for i in range(int((n+1)/2)):
    print(f"{int((n-count)/2)*minus}{star*count}{int((n-count)/2)*minus}")
    count += 2
for i in range(int(n/2)):
    print(f"{wall}{(n-2)*star}{wall}")