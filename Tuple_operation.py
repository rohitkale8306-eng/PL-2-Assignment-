# Python Program: Tuple Operations

# 1. Creating a Tuple
my_tuple = (10, 20, 30, 40, 50)
print("Created Tuple:", my_tuple)


# 2. Accessing Elements
print("Access Element at Index 2:", my_tuple[2])   # Accessing the 3rd element


# 3. Slicing a Tuple
print("Access Elements from Index 1 to 3:", my_tuple[1:4])


# 4. Nested Tuple
nested_tuple = (1, 2, (3, 4, 5), 6)
print("Nested Tuple:", nested_tuple)
print("Access Inner Tuple Element (Index 2, Sub-Index 1):", nested_tuple[2][1])


# 5. Repetition of Tuple
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)


# 6. Concatenation of Tuples
tuple1 = (100, 200, 300)
tuple2 = (400, 500, 600)
concat_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concat_tuple)

