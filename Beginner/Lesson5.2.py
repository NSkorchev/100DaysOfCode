target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total_sum_even = 0

for number in range(2, target + 1, 2):
  if number % 2 == 0:
    total_sum_even += number

print(total_sum_even)