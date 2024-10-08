# lambda function = function written in 1 line using lambda keyword accepts any numbers of arguments,
#                   but only has one expression.(think of it as a shortcut)
#                   (Useful if needed for a short period of time. through-away)

# lamda argument:expression

'''
def double(x):
    return x * 2

print(double(5))

'''

double = lambda x: x*2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z

full_name = lambda first_name, last_name: first_name + ' ' + last_name

print(add(5,6,3))

print(multiply(8, 7))

print(double(5))

print(full_name('Tanvir', 'Hasan'))