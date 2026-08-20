names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# 1. Zip the lists together
zipped_data = zip(names, scores)

# 2. Convert to a list to view the paired tuples
print("Zipped List:", list(zipped_data))
# Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# 3. Common use case: Looping through multiple lists at once
for name, score in zip(names, scores):
    print(f"🔹 {name} scored {score} points.")
