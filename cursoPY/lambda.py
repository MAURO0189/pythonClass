add = lambda a,b: a + b
print(add(10,4))

substract = lambda a,b: a - b
print(substract(8,20))

multiply = lambda a,b: a * b
print(multiply(5,5))

divide = lambda a,b: a / b
print(divide(10,2))


# The lambda keyword is used to create anonymous functions.
# Cuadrado de cada numero

numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)


# Filter
evens_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(evens_numbers)