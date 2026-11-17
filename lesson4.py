# 1. Creates count = 0.
# 2. Uses a for loop to visit numbers from 1 through 20.
# 3. Counts how many numbers are divisible by 3.
# 4. Prints the final count.

count = 0
for i in range(1,21):
    if i % 3 == 0:
        count += 1

print(count)
print("Learning Git is fun!")