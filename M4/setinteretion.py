# Define two sample sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Method A: Using the & operator (Shortest)
intersection_operator = set_a & set_b

# Method B: Using the .intersection() method
intersection_method = set_a.intersection(set_b)

print("Intersection elements:", intersection_operator)
# Output: {4, 5}
