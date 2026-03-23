# PL2 Assignment
# Python Program: Set Operations


# 2.1 Create and Access Set Elements
set_a = {10, 20, 30, 40, 50}
print("Created Set A:", set_a)

print("Accessing elements of Set A:")
for element in set_a:
    print(element, end=" ")
print()


# 2.2 Union of the Elements
set_b = {40, 50, 60, 70, 80}
print("\nSet B:", set_b)

union_set = set_a.union(set_b)
print("Union of Set A and Set B:", union_set)


# 2.3 Intersection of the Elements
intersection_set = set_a.intersection(set_b)
print("Intersection of Set A and Set B:", intersection_set)


# 2.4 Difference of the Elements
difference_set_a_b = set_a.difference(set_b)
print("Difference of Set A - Set B:", difference_set_a_b)

difference_set_b_a = set_b.difference(set_a)
print("Difference of Set B - Set A:", difference_set_b_a)


# 2.5 Symmetric Difference of the Elements
symmetric_diff = set_a.symmetric_difference(set_b)
print("Symmetric Difference of Set A and Set B:", symmetric_diff)


# 2.6 Adding an Element to Set
set_a.add(90)
print("Set A after adding element 90:", set_a)


# 2.7 Removing an Element from Set
set_a.remove(20)
print("Set A after removing element 20:", set_a)


# 2.8 Length of Set
print("Length of Set A:", len(set_a))
