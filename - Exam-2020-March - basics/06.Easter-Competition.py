easter_cake = int(input())
sum = 0
max_baker = ""
max_score = 0

for i in range(easter_cake):
    baker = input()
    score = input()
    sum = 0
    while score != "Stop":
        rate = int(score)
        sum += rate
        score = input()
    if sum > max_score:
        max_score = sum
        max_baker = baker
        print(f"{max_baker} has {max_score} points.")
        print(f"{max_baker} is the new number 1!")
    else:
        print(f"{baker} has {sum} points.")

print(f"{max_baker} won competition with {max_score} points!")


