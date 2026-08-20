import random

def get_well_wishes(name):
    wishes = [
        f"Hope you're having an amazing day, {name}! ✨",
        f"Wishing you nothing but happiness and success today, {name}! 🚀",
        f"May your day be full of good news and clear skies, {name}! ☀️",
        f"Sending you positive vibes and great energy, {name}! 🌱",
        f"Keep shining and crushing your goals, {name}! 💪"
    ]
    # Pick and return one random wish from the list
    return random.choice(wishes)

# Example usage
friend_name = "Alex"
print(get_well_wishes(friend_name))
