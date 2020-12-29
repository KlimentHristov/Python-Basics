cakeWidth = int(input())
cakeLength = int(input())
allCake = cakeWidth * cakeLength

random = input()
while random != "STOP":
    allCake -= int(random)
    if allCake < 1:
        break
    random = input()
if allCake >= 1:
    print(f"{allCake} pieces are left.")
else:
    print(f"No more cake left! You need {abs(allCake)} pieces more.")


