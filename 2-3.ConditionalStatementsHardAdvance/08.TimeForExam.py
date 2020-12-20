import math
hourExam = int(input())
minutesExam = int(input())
hourArrive = int(input())
minutesArrive = int(input())

totalExam = (hourExam * 60) + minutesExam
totalArrive = (hourArrive * 60) + minutesArrive
result = 0
result2 = 0
reminder = 0
if totalExam < totalArrive:
    result = totalArrive - totalExam
    if result > 60:
        result2 = result
        reminder = result2 % 30
        result2 /=30
        result //=60
        print("Late")
        print(f"{result}:{result2:.0f}{reminder} hours after the start")
    else:
        print("Late")
        print(f"{result} minutes after the start")
elif totalExam >= totalArrive:
    result = totalExam - totalArrive
    if result > 30:
        if result > 60:
            result2 = result
            reminder = result2 % 30
            result //= 60
            print("Early")
            print(f"{result}:{reminder} hours before the start")
        elif result == 60:
            result = 1
            reminder = 0
            print("Early")
            print(f"{result}:{reminder}{reminder}hours before the start")
        else:
            print("Early")
            print(f"{result} minutes before the start")
    else:
        if result > 60:
            result2 = result
            reminder = result2 % 30
            result2 /= 30
            result //= 60
            print("On time")
            print(f"{result}:{result2:.0f}{reminder} hours after the start")
        else:
            print("On time")
            print(f"{result} minutes before the start")






