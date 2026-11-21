import math
x = float(input("Number "))

sigmoid_function = 1/(1 + math.exp(-x))

print(sigmoid_function)
