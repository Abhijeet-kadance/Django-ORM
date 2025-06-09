### BASIC COMPREHENSION

# values = []

# for i in range(10):
#     values.append(i)


# values = [ i for i in range(10) ]
# print(values)

# values = [ i + 1 for i in range(10) ]
# print(values)

###### Get all the ven numbers from 0 to 50 (0-50)

# even = []

# for i in range(50):
#     if i % 2 == 0:
#         even.append(i)


# list name = [ value for i in range(50) condition ]

#evens =  [ i for i in range(50) if i % 2 == 0]

### if -else ( inline conditional expression )

# labels = [ 'Even' if x % 2 == 0 else 'odd' for x in range(20) ]

### Nested loops 

# pairs = [(x,y) for x in range(3) for y in range(3)]


### Flattening a matrix ( Nexted List Comprehension )

matrix = [[1,2],[3,4],[5,6]]

# flattened = [ num for row in matrix for num in row]

### Calling Functions

# words = ["hello","world"]
# uppercase = [ word.upper() for word in words ]

### Using with enumerate() or zip()
# indexed = []
# for i,val in enumerate(['a','b','c']):
#     indexed.append(f"{i}: {val}")
# indexed = [f"{i}: {val}" for i, val in enumerate(['a', 'b', 'c'])]

## pythonic way 

# indexed = { i:val for i,val in enumerate(['a','b','c'])}

# zipped = [ x + y for x, y in zip([1,2,3],[10,20,30])]

### Type casting and expressions

# floats = [float(x) for x in range(5)]
# formatted = [f"Item {x}" for x in range(3)]

### With any(),all(),sum(),max(),min()

# has_even = any(x % 2 == 0 for x in range(10))
# total = sum(x for x in range(5))


# print(total)

####################################################
# Create a list of sqaures of numbers from 1 to 10 #
####################################################

# squares = [x**2 for x in range(1,11)]
# print(squares)

##########################################
# Convert a list of strings to uppercase #
##########################################

# words = ['apples','oranges']
# uppercase_words = [w.upper() for w in words]
# print(uppercase_words)

#################################
# Filter even numbers from list #
#################################

# nums = [1,2,3,4,5,6,7,8]
# evens = [num for num in nums if num % 2 == 0]
# print(evens)

########################################
# Get the lengths of strings in a list #
########################################

# names = ['Alice','Bob','Charlie']
# length_string = [len(st) for st in names]
# print(length_string)

###################
# Flatten 2D list #
###################

# matrix = [[1,2],[3,4],[5,6]]
# flat = [num for row in matrix for num in row]
# print(flat)