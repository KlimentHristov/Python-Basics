import math

length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length*width*height
allLiters = volume/1000

aquariumLiters = (allLiters*percent)/100
finalLiters = allLiters - aquariumLiters

print(f"{finalLiters:.3f}")
