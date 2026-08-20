import array as arr

# 1. Create an integer array (typecode 'i')
numbers = arr.array('i', [10, 20, 30, 40])

# 2. Access elements by index
print("First item:", numbers[0])   # 10
print("Last item:", numbers[-1])   # 40

# 3. Add items
numbers.append(50)          # Adds to the end
numbers.insert(1, 15)       # Inserts 15 at index position 1

# 4. Remove items
numbers.remove(30)          # Removes the value 30

print("Modified Array:", numbers)
