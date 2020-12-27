import sys

random = input()
positiveNum = -sys.maxsize
negativeNum = sys.maxsize
currentNum = None

while random != "Stop":
    currentNum = int(random)
    if currentNum <= negativeNum:
        negativeNum = currentNum
    random = input()
if currentNum > negativeNum:
    print(negativeNum)
else:
    print(currentNum)