# GENERATOR -> A function that uses yield to produce values one at a time,
# pausing its execution and resuming from where it left off.

def test():
    yield 10 # yield gives the value and pause the function until the next is asked.
    yield 20

x = test() # x is a created generator object.

print(next(x)) # asks generator for a value.
print(next(x)) # resumes from where it paused.
# print(next(x)) # stopiteration

# Every generator is an iterator, but not every iterator is a generator.



# mainly used to use memory efficiently.
numbers = list(range(1, 100001)) # stores all 100,000 numbers in memory.

def numbers():
    for i in range(1, 100001): # only needed value is produced at that moment.
        yield i

x = numbers()

print(next(x))
print(next(x))
print(next(x))
