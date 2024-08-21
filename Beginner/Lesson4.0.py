# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

heads = 1
tails = 0
random_heads_tails = random.randint(0, 1)
if random_heads_tails == 1:
    print("Heads")
else:
    print("Tails")