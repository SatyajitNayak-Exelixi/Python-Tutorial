# set = set()    # This is am empty set.

sets = {1, 3, 5,6, 5,5} 

print(sets) #It  wont repeat the same element.

#####################################################

# Define two sets
set1 = {1, 3, 4, 5, 6, 7}
set2 = {4, 5, 8, 9}

# UNION: combines all unique elements from both sets
union_set = set1.union(set2)
print("Union:", union_set)

# INTERSECTION: common elements in both sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)


#####################################################

# Create the set
my_set = {1, 3, 4, 5, 6, 7, 87, 5, 4}

# Print the set (duplicates removed automatically)
print(my_set)

# Add an element
my_set.add(10)
print(my_set)

# Remove an element
my_set.remove(3)      # error if element not present
# my_set.discard(99)  # safe remove (no error)

print(my_set)

# Check if element exists
print(5 in my_set)

# Length of set
print(len(my_set))

# Iterate through set
for item in my_set:
    print(item)

# Remove and return a random element
removed_item = my_set.pop()
print("Removed:", removed_item)
print(my_set)

# Clear the set
# my_set.clear()
# print(my_set)
