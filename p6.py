# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print(my_set)


# Distinguish set and dictionary while creating empty set

# initialize a with {}
a = {}

# check data type of a
print(type(a))

# initialize a with set()
a = set()

# check data type of a
print(type(a))

# add an element
# Output: {1, 2, 3}
my_set.add(9)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([8, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([9, 5], {1, 7, 8})
print(my_set)

my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError
<<<<<<< HEAD

=======
>>>>>>> 63c18abe6a3e99cb5199251558c4cf6c4b3f3197
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}


# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
print(A - B)
print(A & B)
print(A ^ B)
