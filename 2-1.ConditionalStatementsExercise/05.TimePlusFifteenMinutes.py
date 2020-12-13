hour = int(input())
seconds = int(input())
addTime = 15
resultSeconds = seconds + addTime

if resultSeconds >= 60:
    hour +=1
    resultSeconds -= 60
if hour > 23:
    hour = 0

if resultSeconds < 10:
    print(f"{hour}:"f"0" + f"{resultSeconds}")
else:
    print(f"{hour}"f":{resultSeconds}")
