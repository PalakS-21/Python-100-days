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


# Generator Expressions -> used for something simple, u can write in one line.

# list expression -> []
numbers = [x * 2 for x in range(5)]
print(numbers)
print("\n")

# generator expression -> ()
numbers = (x * 2 for x in range(5))
print(numbers)
 # it doen't print actual numbers, it gives us generator object

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

print(type(x))

x = (i * 3 for i in range(5))

print(next(x))
print(next(x))
print("After next...")

for n in x:
    print(n) # it continues from where it left, it does not restart

# GENERATOR FUNCTION -> use when u have multiple steps or some logic.

# Generate numbers on demand.
def numbers(n):
    for i in range(1, n + 1):
        yield i
        # yield i * i

n = int(input("How many numbers? "))

for number in numbers(n):
    print(number)



def even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter number: "))

for number in even_numbers(n):
    print(number)

#------------------------------------------------------------------

# yield from -> yield each value from the iterable one by one.
def numbers():
    yield from [10, 15, 20, 25, 30]

for number in numbers():
        print(number)

#---------------------------------------------------------------

def fruits():
    yield "Apple"
    yield "Banana"
    yield "Mango"

def all_items():
    yield from fruits()
    yield "Milk"
    yield "Bread"

for item in all_items():
    print(item)