def find_largest(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i

    return largest