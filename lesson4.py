
def find_largest(numbers):

  if len(numbers) == 0:
      return None
  
  largest = numbers[0]
  
  for i in numbers:
      if i > largest:
          largest = i
  
  return largest
          

        


print(find_largest([4, 9, 2, 15, 7]))
print(find_largest([]))
print(find_largest([-8, -3, -12]))