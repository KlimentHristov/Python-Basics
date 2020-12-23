openTabs = int(input())
salary = int(input())

penalty = 0

for i in range(openTabs):
    openSites = input()
    if openSites == "Facebook":
        penalty = 150
    elif openSites == "Instagram":
        penalty = 100
    elif openSites == "Reddit":
        penalty = 50
    else:
        penalty = 0
    salary -=penalty
    if salary <= 0:
        print("You have lost your salary.")
        break
if salary > 0:
    print(salary)
