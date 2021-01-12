minutes = int(input())
count_walking = int(input())
calories_per_day = int(input())

all_minutes_walking = minutes * count_walking
all_calories_per_day = all_minutes_walking * 5

if float((calories_per_day / 2)) <= all_calories_per_day:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {all_calories_per_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {all_calories_per_day}.")

