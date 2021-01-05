juri = int(input())
saveJuri = juri
sum = 0
average = 0
presentation = ""
averageSum = 0
averageSumCount = 0
while presentation != "Finish":
    presentation = input()
    if presentation == "Finish":
        break
    while juri > 0:
        rate = float(input())
        sum += rate
        juri -=1
    average = float(sum / saveJuri)
    averageSum += average
    averageSumCount +=1
    sum = 0
    print(f"{presentation} - {average:.2f}.")
    juri = saveJuri
print(f"Student's final assessment is {(averageSum/averageSumCount):.2f}.")
