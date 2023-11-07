# The zip() function takes iterables (can be zero or more),
# aggregates them in a tuple, and returns it.

languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print(result)
print(list(result))


# Example 1:

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()
print('zip() - No iterables are passed')

# Converting iterator to list
result_list = list(result)
print(result_list, 'Converting iterator to list')


# Two iterables are passed
result = zip(number_list, str_list)
print(result, 'Two iterables are passed')

# Converting iterator to set
result_set = set(result)
print(result_set, 'Converting iterator to set')


# Example 2: Different number of iterable elements

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)


# Example 3: Unzipping the Value Using zip()

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v =  zip(*result_list)
print('c =', c)
print('v =', v)


# Example 4: Create dict from 2 lists:

a = [1, 2, 3, 4, 5, 6]
b = ['a', 'b', 'c', 'd', 'e', 'f']

c = {}

# for i in range(len(a)):
#     c[a[i]] = b[i]
# print(c)
#OR
c = dict(list(zip(a, b)))
print(c)
