oneMeter = 1000 # mm
oneMeter_another = 100 # cm
oneCentimeter = 10 #mm

howMany = float(input())
random = str(input())
transform = str(input())

if random == "m":
    if transform == "cm":
        howMany *= 100
    else:
        howMany *= 1000
elif random == "cm":
    if transform == "mm":
        howMany *= 10
    else:
        howMany /= 100
elif random == "mm":
    if transform == "cm":
        howMany /= 10
    else:
        howMany /= 1000

print(f"{howMany:.3f}")
