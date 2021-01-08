import math
hour_per_exam = int(input()) * 60
min_per_exam = int(input())

hour_per_arrive = int(input()) * 60
min_per_arrive = int(input())

total_time_arrive = hour_per_arrive + min_per_arrive
total_time_exam = hour_per_exam + min_per_exam
true_time = total_time_exam - total_time_arrive #min Early

# 13:00 Exam  ==  13:00 arrive or Exam <= 30 min.
if 0 <= true_time <= 30:
    print("On Time")
# 13:00 Exam > 12:10 arrive
elif true_time > 30:
    print('Early')
# 13:00 Exam  <  13:05 arrive
else:
    print('Late')

# second condition
if 0 <= true_time <= 59:
    print(f"{true_time} minutes before the start")
elif true_time >= 60:
    if true_time % 60 < 10:
        print(f"{math.floor(true_time/60)}:0{true_time%60} hours before the start")
    else:
        print(f"{math.floor(true_time / 60)}:{true_time % 60} hours before the start")
else:
    if abs(true_time) <= 59:
        if abs(true_time) < 10:
            print(f"{abs(true_time)} minutes after the start")
        else:
            print(f"{abs(true_time)} minutes after the start")
    else:
        if abs(true_time) % 60 < 10:
            print(f"{math.floor(abs(true_time / 60))}:0{abs(true_time % 60)} hours after the start")
        else:
            print(f"{math.floor(abs((true_time / 60)))}:{abs(true_time % 60)} hours after the start")
