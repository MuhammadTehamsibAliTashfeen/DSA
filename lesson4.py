def find_second_largest(numbers):
    
    if len(numbers) == 0:
        return None
    
    largest = numbers[0]
    
    for i in numbers:
        if i > largest:
            largest = i
    
    second = numbers[0]
    
    for i in numbers:
        if largest > i and i > second:
            second = i
    return second
        
    
    
    
    
    
    
print(find_second_largest([12, 7, 25, 18, 25]))
print(find_second_largest([5, 5, 5]))
print(find_second_largest([10]))
print(find_second_largest([]))
print(find_second_largest([-8, -3, -12]))