rent = int(input())

cake = rent * 0.2 # 20 %
drinks = cake - (cake * 0.45) # 45% minus cake
animator = rent / 3

allSum = rent + cake + drinks + animator

print(allSum)