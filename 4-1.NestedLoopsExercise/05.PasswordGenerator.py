n = int(input())
l = int(input())

for indexOne in range(1,n+1): # 2
    for indexTwo in range(1,n +1): #
        for indexThree in range(97,97+l):
            for indexFour in range(97, 97+l):
                for indexFive in range(1,n+1):
                    if indexFive > indexOne and indexFive > indexTwo:
                        print(f"{indexOne}{indexTwo}{chr(indexThree)}{chr(indexFour)}{indexFive}", end=" ")