negative = int(input())
text = ""
countNegative = 0
counter = 0
sum = 0
nameCounter = 0

while text != "Enough":
    nameProblem = input()
    if nameProblem == "Enough":
        break
    lastProblem = nameProblem
    nameCounter += 1
    rate = int(input())
    sum += rate
    counter += 1
    if rate <= 4:
        countNegative += 1
    if countNegative == negative:
        print(f"You need a break, {negative} poor grades.")
        break
average = sum / counter
if countNegative == negative:
    pass
else:
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {nameCounter}")
    print(f"Last problem: {lastProblem}")



