import math

year = input() # leap or normal year
p = int(input()) # count vacations which not sunday or saturday
h = int(input()) # count weeks which vlady go to home city

allWeeks = 48

if year == "normal":
    allWeeks -= h # days which vlady go to home city
    allWeeks = (allWeeks * 3) / 4 # 3/4 days is not on work (Saturday games in Sofia)
    # in home city h are more games wich can calculate later or plus allWeeks
    p = (p * 2)/3 # games in vacations days
    allWeeks = p + h + allWeeks # all games

elif year == "leap":
    allWeeks -= h # days which vlady go to home city
    allWeeks = (allWeeks * 3) / 4 # 3/4 days is not on work (Saturday games in Sofia)
    # in home city h are more games wich can calculate later or plus allWeeks
    p = (p * 2)/3 # games in vacations days
    allWeeks = p + h + allWeeks # all games
    allWeeks = allWeeks + (allWeeks * 0.15)

print(math.floor(allWeeks))



