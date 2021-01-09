n = int(input())
star = '*'
symb = '//'
empty = " "
wall = '|'

print(f"{n * 2 * star}{n * empty}{n * 2 * star}")

for row in range(1, n - 1):
    if n % 2 == 0:
        if row == n / 2 - 1:
            print(f"{star}{(n - 1) * symb}{star}{n * wall}{star}{(n - 1) * symb}{star}")
        else:
            print(f"{star}{(n - 1) * symb}{star}{n * empty}{star}{(n - 1) * symb}{star}")
    else:
        if row == (n - 1) / 2:
            print(f"{star}{(n - 1) * symb}{star}{n * wall}{star}{(n - 1) * symb}{star}")

        else:
            print(f"{star}{(n - 1) * symb}{star}{n * empty}{star}{(n - 1) * symb}{star}")

print(f"{n * 2 * star}{n * empty}{n * 2 * star}")