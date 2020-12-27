import sys

random = input()
positiveNum = -sys.maxsize
negativeNum = sys.maxsize

while random != "Stop":
    currentNum = int(random)
    if currentNum >= positiveNum:
        positiveNum = currentNum
    if currentNum >= negativeNum:
        negativeNum = currentNum
    random = input()

if positiveNum >= currentNum:
    print(positiveNum)
else:
    print(negativeNum)