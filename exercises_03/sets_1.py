# Creating a set with some elements
my_set = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}

# Displaying the original set
print("Original Set:", my_set)

# Adding elements to the set
my_set.add(8)
my_set.add(7)

# Displaying the set after adding elements
print("Set after adding elements:", my_set)

# Removing an element from the set
my_set.remove(2)

# Displaying the set after removing an element
print("Set after removing '2':", my_set)

# Performing set operations (union, intersection)
other_set = {2, 7, 1, 4}
union_result = my_set.union(other_set)
intersection_result = my_set.intersection(other_set)

# Displaying the results of set operations
print("Union of the sets:", union_result)
print("Intersection of the sets:", intersection_result)
