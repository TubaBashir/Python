# 1. Creating a tuple
coordinates = (4, 5, 12, 4, 8)
print("Original Tuple:", coordinates)

# Note: To create a tuple with only ONE item, you MUST include a trailing comma
single_item_tuple = ("apple",) 

# 2. Accessing items by index
print("First item:", coordinates[0])   # 4
print("Last item:", coordinates[-1])   # 8

# 3. Slicing a subset
print("Middle items:", coordinates[1:4])  # (5, 12, 4)
