
# append() -> add one element at end

nums = [3, 23, 56, 12, 21, 8, 77]
print(nums)
nums.append(99)

print(nums)

# sort() -> arranging numbers in ascending / descending order

nums.sort()  # ascending order
print(nums)

nums.sort(reverse=True)  # descending order
print(nums)

# reverse() ->  reverses the list

nums = [3, 23, 56, 12, 21, 8, 77]

nums.reverse()
print(nums)

# index() -> find position

nums = [3, 23, 56, 12, 21, 8, 77, 23]

print(nums.index(77))
print(nums.index(56))

# count() -> counts the number of occurence of a number in a list

nums = [3, 23, 56, 12, 21, 8, 77, 23]

print(nums.count(23))
print(nums.count(21))
print(nums.count(11))

# extend() -> add multiple elements

nums = [1, 2, 3]
nums.extend([4, 5, 6])

print(nums)

# insert(index, value) -> add at specific position

nums = [2, 4, 6]
nums.insert( 3, 8)
nums.insert(2, 10)
print(nums)

# remove() -> remove specific value (first occurence only)

nums = [1, 2, 3, 2]
nums.remove(2)

print(nums) # [1,3]

# pop() -> removes last element(by default), also removes using index

nums = [1, 2, 3, 4, 5]
nums.pop() # removes last element

print(nums)

nums = [1, 2, 3, 4, 5]
nums.pop(2) # removes element on 2nd index

print(nums)

# clear() -> remove all elements

nums = [2, 4, 6, 0, 32, 8]
nums.clear()

print(nums) # []

# max() / min()

nums = [2, 4, 6, 0, 32, 8]

print(max(nums))
print(min(nums))

# sum() -> sum of list elements

nums = [1, 2, 3, 4, 5]

print(sum(nums))

# copy() -> new list (create a copy without changing the original one)

a = [1, 2, 3, 4, 5]
b = a.copy()

b.append(6)

print(a) # original list
print(b) # new list

# without copy(), it changes the original list also

x = [10, 20, 30, 40, 50]
y = x  # a and b are pointing to SAME list in memory

y.append(60)

print(x) #original also changed
print(y)

# some more examples

a = [[2, 3], [4, 5]] # [[list 1 -> index 0], [list 2 -> index 1]]
b = a.copy()

b[1][1] = 8  # 2nd list -> 1st index -> 8

print(a)
print(b)