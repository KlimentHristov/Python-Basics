days = int(input())
food = float(input())
sumFood = 0
biscuits = 0
dog_counter = 0
cat_counter = 0

for i in range(1,days+1):
    dog_food = float(input())
    dog_counter +=dog_food

    cat_food = float(input())
    cat_counter += cat_food

    if i % 3 == 0:
        biscuits += (dog_food+cat_food)*0.1

    sumFood += (dog_food + cat_food)

print(f"Total eaten biscuits: {biscuits:.0f}gr.")
print(f"{float((sumFood/food)*100):.2f}% of the food has been eaten.")
print(f"{float((dog_counter/sumFood)*100):.2f}% eaten from the dog.")
print(f"{float((cat_counter/sumFood)*100):.2f}% eaten from the cat.")
