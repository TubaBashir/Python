sentence = "apple banana apple cherry apple grape"
target = "apple"

# Split sentence into individual words
words = sentence.split()

# 1. Count occurrences
count = words.count(target)

# 2. Find all index positions
positions = [index for index, word in enumerate(words) if word == target]

print(f"The word '{target}' appears {count} times.")
print(f"It appears at word positions: {positions}")
