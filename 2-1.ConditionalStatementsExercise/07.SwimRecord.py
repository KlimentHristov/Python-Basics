recordSec = float(input())
distance = float(input())
timeInSeconds = float(input())
result = distance * timeInSeconds
# time slow
delay = (distance // 15) * 12.5
result += delay

if result < recordSec:
    print(f"Yes, he succeeded! The new world record is {result:2.f} seconds.")
else:
    print(f"No, he failed! He was {result - recordSec:.2f} seconds slower.")



