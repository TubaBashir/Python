# 1. Create sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# 2. Add and Remove items
set_a.add(6)        # Adds an item
set_a.discard(1)    # Removes an item safely (won't crash if item doesn't exist)

print("Set A modified:", set_a)
