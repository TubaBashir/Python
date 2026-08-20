import math

def run_practice_arena():
    print("🧠 WELCOME TO THE PYTHON COMPREHENSION PRACTICE ARENA 🧠")
    print("Transform standard 'for' loops into clean, professional one-liners.\n")

    # ----------------------------------------------------
    # CHALLENGE 1: List Comprehension (Filtering & Math)
    # Goal: Take a list of numbers, keep only the odd ones, and cube them.
    # ----------------------------------------------------
    print("--- CHALLENGE 1: Odd Cubes ---")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Standard Loop Version:
    # loop_res = []
    # for x in numbers:
    #     if x % 2 != 0:
    #         loop_res.append(x**3)
    
    # Your Task: Complete the list comprehension line below
    ch1_solution = [x**3 for x in numbers if x % 2 != 0]
    print(f"Original: {numbers}")
    print(f"Result:   {ch1_solution}\n")


    # ----------------------------------------------------
    # CHALLENGE 2: Dictionary Comprehension (Mapping)
    # Goal: Take a list of names and map each name to its character length.
    # ----------------------------------------------------
    print("--- CHALLENGE 2: Name Length Map ---")
    names = ["Alice", "Bob", "Charlie", "Dan"]
    
    # Your Task: Complete the dictionary comprehension line below
    ch2_solution = {name: len(name) for name in names}
    print(f"Original: {names}")
    print(f"Result:   {ch2_solution}\n")


    # ----------------------------------------------------
    # CHALLENGE 3: Conditional If-Else Comprehension
    # Goal: Mark temperatures as "Hot" if 30 or above, otherwise "Cool".
    # ----------------------------------------------------
    print("--- CHALLENGE 3: Weather Labeler ---")
    temps = [22, 35, 18, 30, 15, 42]
    
    # Your Task: Complete the inline If-Else comprehension line below
    ch3_solution = ["Hot" if t >= 30 else "Cool" for t in temps]
    print(f"Original: {temps}")
    print(f"Result:   {ch3_solution}\n")


    # ----------------------------------------------------
    # CHALLENGE 4: Set Comprehension (Deduplication)
    # Goal: Extract unique, lower-case initials from a phrase, ignoring spaces.
    # ----------------------------------------------------
    print("--- CHALLENGE 4: Unique Initials Set ---")
    phrase = "Python Programming Playground Paradox"
    
    # Your Task: Complete the set comprehension line below (uses curly braces)
    ch4_solution = {word[0].lower() for word in phrase.split()}
    print(f"Original String: '{phrase}'")
    print(f"Resulting Set:   {ch4_solution}\n")


    # ----------------------------------------------------
    # CHALLENGE 5: Advanced Nested Comprehension (Matrix Flattening)
    # Goal: Convert a 2D matrix layout table into a single flat list of integers.
    # ----------------------------------------------------
    print("--- CHALLENGE 5: Matrix Flattener ---")
    matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    
    # Your Task: Complete the nested flattening layout line below
    ch5_solution = [item for row in matrix for item in row]
    print(f"Original Matrix: {matrix}")
    print(f"Flattened List:  {ch5_solution}\n")

if __name__ == "__main__":
    run_practice_arena()
