daysCount = int(input())

count_win_per_day = 0
count_win =0
count_lose_per_day = 0
count_lose = 0

sumWin = 0
sumDays = 0

for i in range(1,daysCount+1):
    game = input()
    sumDays += sumWin
    sumWin = 0
    count_win_per_day = 0
    count_lose_per_day = 0
    while game != 'Finish':
        result = input()
        if result == "win":
            count_win_per_day += 1
            count_win +=1
            sumWin += 20
        elif result == "lose":
            count_lose_per_day += 1
            count_lose +=1
        game = input()

    if count_win_per_day > count_lose_per_day:
        sumWin = float(sumWin + ((sumWin * 10) / 100))

sumDays += sumWin
if count_win > count_lose:
    sumDays = float((sumDays + (sumDays *20)/100))
    print(f"You won the tournament! Total raised money: {(sumDays):.2f}")
else:
    print(f"You lost the tournament! Total raised money: {(sumDays):.2f}")