
def reverse_list(numbers):
    reversed_numbers = []
    for i in range(len(numbers)-1,-1,-1):
        reversed_numbers.append(numbers[i])
    return reversed_numbers
            
            
print(reverse_list([10, 20, 30, 40, 50]))
print(reverse_list([1]))
print(reverse_list([]))
print(reverse_list([-3, 0, 7]))