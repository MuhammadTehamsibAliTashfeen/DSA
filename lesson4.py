# Write a function that:
# 1. Is named find_smallest(numbers).
# 2. Accepts a list as its parameter.
# 3. Finds the smallest value without using min().
# 4. Returns the smallest value after examining the list.
# 5. Works with negative numbers.
def find_smallest(numbers):
    smallest = numbers[0]
    
    for i in numbers:
        if i < smallest:
            smallest = i
    
    return smallest



print(find_smallest([8, -4, 15, -12, 3]))