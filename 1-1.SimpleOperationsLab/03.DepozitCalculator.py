depozit = int(input())
timeDepozit = float(input())
yearInterest = float(input())


interest = (depozit * yearInterest)/100
interest /=12

finalSum = depozit + (timeDepozit*interest)
print(finalSum)