import random as rnd

test_seed = int(input("Create a seed A Number ...:"))

rnd.seed(test_seed)

names = input("Give me people names separated by a , :\n").strip().split(", ")
len = len(names)
print(f"{names[rnd.randint(0,len -1)]} is Going to pay the Pill")
print(f"{rnd.choice(names)} is Going to pay the Pill")
