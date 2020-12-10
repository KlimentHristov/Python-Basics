import math

dogs = int(input())
pack = 2.50
restDogs = int(input())
restPack = 4

dogExpense = dogs * pack
restExpense = restDogs * restPack

allExpense = dogExpense + restExpense

print(f"{allExpense:.2f} lv.")
