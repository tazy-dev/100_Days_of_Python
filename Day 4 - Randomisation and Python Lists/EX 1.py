import random as rnd

test_seed = int(input("Create a seed A Number ...:"))

rnd.seed(test_seed)

if rnd.randint(0,1) == 1 : print("Heads") 
else: print("Tails")