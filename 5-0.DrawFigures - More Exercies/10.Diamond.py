n = int(input())
star = '*'
minus = '-'

left_right = int((n-1)/2) # left and right
mid = (n-2) * (left_right -2) # middle

if n <= 1:
    print("*")
elif n % 2 == 0:
    for i in range(1,int(n/2)):
        if i == 1:
            print(f"{left_right*minus}{star}{star}{left_right*minus}")
            mid = 0
        else:
            mid+=2
            print(f"{left_right * minus}{star}{mid * minus}{star}{left_right * minus}")
        left_right -=1
    print(f"{star}{(n-2)*minus}{star}")
    for y in reversed(range(1,int(n/2))):
            left_right +=1
            print(f"{left_right * minus}{star}{mid * minus}{star}{left_right * minus}")
            mid -=2
else:
        for z in range(1,int(n/2+1)):
            if z == 1:
                print(f"{left_right*minus}{star}{left_right*minus}")
                mid = 1
            else:
                left_right -= 1
                print(f"{left_right * minus}{star}{mid * minus}{star}{left_right * minus}")
                mid +=2
        print(f"{star}{(n-2)*minus}{star}")
        for x in reversed(range(1,int(n/2))):
            mid -= 2
            print(f"{left_right * minus}{star}{mid * minus}{star}{left_right * minus}")
            left_right +=1
        print(f"{left_right * minus}{star}{left_right * minus}")



