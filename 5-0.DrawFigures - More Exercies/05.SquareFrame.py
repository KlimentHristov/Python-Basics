plus = '+'
minus = '- '
wall = '|'
empty = " "

n = int(input())

#start
print(f"{plus}{empty}{(n-2)*minus}{plus}")
# middle
for item in range(1,n-1):
    print(f"{wall}{empty}{(n-2)*minus}{wall}")
#end
print(f"{plus}{empty}{(n-2)*minus}{plus}")
