# filter(function, iterable)
numbers = [1,2,3,4,5,6,7,8]
even_number = list(filter(lambda x: x % 2 == 0, numbers))
print(even_number)