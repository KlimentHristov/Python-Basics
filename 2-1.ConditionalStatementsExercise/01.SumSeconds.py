secondsOne = int(input())
secondsTwo = int(input())
secondsThree = int(input())
allSeconds = secondsOne + secondsTwo + secondsThree

minute = 60
count = 0
result = "0"

while allSeconds > minute:
    count += 1
    allSeconds -=minute
if allSeconds < 10:
    print(f"{count}:{0}{allSeconds}")
else:
    print(f"{count}:{allSeconds}")


