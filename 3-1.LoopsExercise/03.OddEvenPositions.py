import sys
random = int(input())

sumEven = 0
evenMax = -sys.maxsize
evenMin = sys.maxsize

sumOdd = 0
oddMin = sys.maxsize
oddMax = -sys.maxsize


for x in range(1,random+1):
    n = float(input())
    if x % 2 == 0:
        sumEven+=n
        if n > evenMax:
            evenMax = n
        if n < evenMin:
            evenMin = n
    else:
        sumOdd +=n
        if n > oddMax:
            oddMax = n
        if n < oddMin:
            oddMin = n

print(f"OddSum={sumOdd:.2f},")
if oddMin != sys.maxsize:
    print(f"OddMin={oddMin:.2f},")
else:
    print(f"OddMin=No,")
if oddMax != -sys.maxsize:
    print(f"OddMax={oddMax:.2f},")
else:
    print(f"OddMax=No,")

print(f"EvenSum={sumEven:.2f},")
if evenMin != sys.maxsize:
    print(f"EvenMin={evenMin:.2f},")
else:
    print(f"EvenMin=No,")
if evenMax != -sys.maxsize:
    print(f"EvenMax={evenMax:.2f}")
else:
    print(f"EvenMax=No")


