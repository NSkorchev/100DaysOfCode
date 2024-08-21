print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name = name1 + name2
lower_name = combined_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
score1 = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
score2 = l + o + v + e

score = int(str(score1) + str(score2))

if 10 >= score or score >= 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.") 