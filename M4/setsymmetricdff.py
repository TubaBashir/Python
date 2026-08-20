# Define two sample sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Method A: Using the ^ operator (Shortest)
sym_diff_operator = set_a ^ set_b

# Method B: Using the .symmetric_difference() method
sym_diff_method = set_a.symmetric_difference(set_b)

print("Unique to either set:", sym_diff_operator)
# Output: {1, 2, 3, 6, 7, 8} (Notice 4 and 5 are removed)
