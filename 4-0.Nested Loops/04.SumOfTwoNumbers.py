first = int(input())
second = int(input())
magicNum = int(input())
combination = 0
isFound = False
allCombinations = 0
for i in range(first, second + 1):
    for x in range(first, second + 1):
        allCombinations += 1
        if i + x == magicNum:
            isFound = True
            break
    if isFound:
        break
if isFound == False:
    print(f"{allCombinations} combinations - neither equals {magicNum}")
else:
    print(f"Combination N:{allCombinations} ({i} + {x} = {magicNum})")
