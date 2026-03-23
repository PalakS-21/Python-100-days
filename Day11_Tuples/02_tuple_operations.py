
# Operations that can be performed on tuples.
# tuples cannot be manipulated until they are converted to a list.

# concatenation(+) -> joins two tuples and makes a new tuple.

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = tup1 + tup2 # new tuple
print(tup3)

# repitition(*) ->

t = (2, 4) # remains unchanged
t2 = t * 3 # repeat 3 times, forms a new tuple
print(t2)

# membership(in, not in) -> checks for an element and returns boolean value.

tup = (10, 20, 30, 40, 50)
print(30 in tup) # returns true?false
print(40 not in tup)

# indexing
print(tup[0])
print(tup[-1])

# loop (iteration)

for x in tup:
    print(x)

# len() -> length
print(len(tup))

# slicing
print(tup[0:3])



# tuple to list conversion

tup = (1, 2, 3)

l = list(tup)
print(l)
print(type(l))

# now after conerting to list, we can manipulate it
l.append(4)
print(l)

# packing in tuple -> putting multiple values into one tuple

tupl = 9, 8, 7, 6, 5  # python automatically creates tuple by default
print(tupl)

# unpacking of tuple -> taking values out of tuples into variables

t = (100, 200, 300, 400, 500)

a, b, c, d, e = t  # no. of variables = no. of element

print(a) # 100
print(b) # 200
print(c) # 300
print(d) # 400
print(e) # 500


# advanced unpacking

t = (100, 200, 300, 400, 500)

a, b, *c = t # * collects reamining values a list

print(a) # 100 - 1st value -> a
print(b) # 200 - 2nd value -> b
print(c) # [300, 400, 500] -> c, remaining values in list form



# packing in function

def func():
    return 5, 10

# unpacking while calling
x, y = func()
print(x)
print(y)


# swapping variables

a = 4
b = 8

a, b = b, a
print(a, b)



# list to tuple conversion
l = [1, 2, 3]
t = tuple(l)

print(t)
