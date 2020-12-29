sumSteps = 0
goal = 10000
steps = input()
saveSteps = None

while steps != "Going home":
    saveSteps = int(steps)
    sumSteps += saveSteps
    if sumSteps >= goal:
        print(f"Goal reached! Good job!")
        print(f"{sumSteps-goal} steps over the goal!")
        break
    steps = input()
if steps == "Going home":
    moreSteps = int(input())
    if sumSteps + moreSteps > goal:
        print(f"Goal reached! Good job!")
        print(f"{(sumSteps+moreSteps) - goal} steps over the goal!")
    else:
        print(f"{goal - (moreSteps + sumSteps)} more steps to reach goal.")
