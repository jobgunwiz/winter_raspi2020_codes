
add = lambda x, y : x+y
print(add(1,2))


#mecro, inline function in C

cal = [lambda x, y: x+y, lambda x, y: x-y, lambda x, y: x*y]

print(cal[0](1,2))
print(cal[1](1,2))
print(cal[2](1,2))
