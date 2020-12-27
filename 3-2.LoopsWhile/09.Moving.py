width = int(input())
lenght = int(input())
heigh = int(input())
cubicRoom = width * lenght * heigh

text = input()
currentBox = 0
sumBox = 0

while text != "Done":
    currentBox = int(text)
    sumBox += currentBox
    if sumBox >= cubicRoom:
        print(f"No more free space! You need {sumBox - cubicRoom} Cubic meters more.")
        break
    text = input()
if cubicRoom > sumBox:
    print(f"{cubicRoom - sumBox} Cubic meters left.")
