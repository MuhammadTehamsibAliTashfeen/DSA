def count_occurrences(numbers, target):
    if len(numbers) == 0:
        return 0
    elif len(numbers) > 0:
        count = 0
        for i in numbers:
            if i == target:
                count +=1
        return count
    
    
    
    
    
    
    
    
print(count_occurrences([2, 4, 2, 6, 2], 2))
print(count_occurrences([1, 3, 5], 7))
print(count_occurrences([], 10))