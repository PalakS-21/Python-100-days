# Iterator -> it is an object that lets us go through elements one by one.
# iter()
# next()

numbers = [10, 20, 30, 40]

my_iter = iter(numbers)

print(next(my_iter)) #10
print(next(my_iter)) #20
print(next(my_iter)) #30
print(next(my_iter)) #40

# basically, iter() acts as a pointer, that points at the first number/element, and then moves to next element sequentially.
# iter() creates an iterator from list.
# next() means the next available element.
