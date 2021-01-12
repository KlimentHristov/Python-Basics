firstPlayerEggs = int(input())
secondPlayerEggs = int(input())
command = ""

while command != "End of battle":
    if firstPlayerEggs <= 0 or secondPlayerEggs <= 0:
        if firstPlayerEggs < secondPlayerEggs:
            print(f"Player one is out of eggs. Player two has {secondPlayerEggs} eggs left.")
        elif secondPlayerEggs < firstPlayerEggs:
            print(f"Player two is out of eggs. Player one has {firstPlayerEggs} eggs left.")
        break
    command = input()
    if command == "one":
        secondPlayerEggs -=1
    elif command == "two":
        firstPlayerEggs -=1
    else:
        break
if command == "End of battle":
    print(f"Player one has {firstPlayerEggs} eggs left.")
    print(f"Player two has {secondPlayerEggs} eggs left.")