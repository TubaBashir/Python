original_list = ["apple", "banana", "apple", "cherry", "banana"]

# Convert to set (removes duplicates) and back to list
clean_list = list(set(original_list))

print("Clean List:", clean_list) 
# Output can be in any order, e.g., ['banana', 'cherry', 'apple']
