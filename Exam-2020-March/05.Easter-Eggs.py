eggs = int(input())
red_counter = 0
orange_counter = 0
blue_counter = 0
green_counter = 0

while eggs > 0:
    currentEgg = input()
    if currentEgg == "red":
        red_counter +=1
    elif currentEgg == "orange":
        orange_counter +=1
    elif currentEgg == "blue":
        blue_counter +=1
    elif currentEgg == "green":
        green_counter +=1
    eggs -=1

print(f"Red eggs: {red_counter}")
print(f"Orange eggs: {orange_counter}")
print(f"Blue eggs: {blue_counter}")
print(f"Green eggs: {green_counter}")

if red_counter > max(orange_counter,blue_counter,green_counter):
    print(f"Max eggs: {max(red_counter,orange_counter,blue_counter,green_counter)} -> red")
elif orange_counter > max(red_counter,blue_counter,green_counter):
    print(f"Max eggs: {max(red_counter, orange_counter, blue_counter, green_counter)} -> orange")
elif blue_counter > max(red_counter,orange_counter,green_counter):
    print(f"Max eggs: {max(red_counter, orange_counter, blue_counter, green_counter)} -> blue")
elif green_counter > max(red_counter,blue_counter,orange_counter):
    print(f"Max eggs: {max(red_counter, orange_counter, blue_counter, green_counter)} -> green")