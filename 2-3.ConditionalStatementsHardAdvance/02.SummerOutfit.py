gradus = int(input())
timeDay = input()

if timeDay == "Morning":
    if gradus >= 10 and gradus <= 18:
        print(f"It's {gradus} degrees, get your Sweatshirt and Sneakers.")
    elif gradus > 18 and gradus <=24:
        print(f"It's {gradus} degrees, get your Shirt and Moccasins.")
    elif gradus >= 25:
        print(f"It's {gradus} degrees, get your T-Shirt and Sandals.")
elif timeDay == "Afternoon":
    if gradus >= 10 and gradus <= 18:
        print(f"It's {gradus} degrees, get your Shirt and Moccasins.")
    elif gradus > 18 and gradus <=24:
        print(f"It's {gradus} degrees, get your T-Shirt and Sandals.")
    elif gradus >= 25:
        print(f"It's {gradus} degrees, get your Swim Suit and Barefoot.")
elif timeDay == "Evening":
    if gradus >= 10 and gradus <= 18:
        print(f"It's {gradus} degrees, get your Shirt and Moccasins.")
    elif gradus > 18 and gradus <=24:
        print(f"It's {gradus} degrees, get your Shirt and Moccasins.")
    elif gradus >= 25:
        print(f"It's {gradus} degrees, get your Shirt and Moccasins.")
