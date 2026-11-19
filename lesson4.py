# Write a program that:
# 1. Searches numbers = [5, 10, 15, 20, 25].
# 2. Sets target = 99.
# 3. Uses linear search with range(len(numbers)).
# 4. Prints "Found at index X" if the target exists, replacing X with the actual index.
# 5. Prints "Not Found" if the target does not exist.
numbers = [5, 10, 15, 20, 25]
target = 99
index = -1

for i in range(len(numbers)):
    if target == numbers[i]:
        print("Found at index",i)
        index = i
        break


if index == -1:
    print("Not Found")
        