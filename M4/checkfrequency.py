from collections import Counter

items = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# 1. Generate frequency map
frequency = Counter(items)

print("Frequency Count:", frequency)
# Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# 2. Access an individual count
print(f"Count of apples: {frequency['apple']}")
