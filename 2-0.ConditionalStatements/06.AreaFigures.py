from math import pi
import math
figure = str(input())

if figure == "square":
    oneSide = float(input())
    areaS = float(oneSide*oneSide)
    print(f"{areaS:.3f}")
elif figure == "rectangle":
    lenghtSide = float(input())
    widthSide = float(input())
    areaR = float(lenghtSide * widthSide)
    print(f"{areaR:.3f}")
elif figure == "circle":
    radius = float(input())
    areaC = pi * pow(radius,2)
    print(f"{areaC:.3f}")
elif figure == "triangle":
    lenghtSide = float(input())
    heightSide = float(input())
    areaT = (lenghtSide * heightSide) /2
    print(f"{areaT:.3f}")