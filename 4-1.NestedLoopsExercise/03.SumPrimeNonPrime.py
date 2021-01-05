randomNum = input()
sumPrime = 0
sumNonPrime = 0
while randomNum != "stop":
    randomNum = int(randomNum)
    if randomNum < 1:
        if randomNum < 0:
            print(f"Number is negative.")
    for i in range(2, randomNum):
        if (randomNum % i) == 0:
            sumNonPrime += randomNum
            break
    else:
        sumPrime += randomNum
    randomNum = input()
if sumPrime < 1:
    sumPrime = 0
print(f"Sum of all prime numbers is: {sumPrime}")
print(f"Sum of all non prime numbers is: {sumNonPrime}")
