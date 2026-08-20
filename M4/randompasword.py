import random
import string

def generate_password(length, use_upper, use_digits, use_special):
    # 1. Start with mandatory lowercase characters
    char_pool = string.ascii_lowercase
    
    # Track mandatory inclusions to ensure the password contains chosen categories
    mandatory_chars = [random.choice(string.ascii_lowercase)]
    
    # 2. Add extra character sets based on user preferences
    if use_upper:
        char_pool += string.ascii_uppercase
        mandatory_chars.append(random.choice(string.ascii_uppercase))
    if use_digits:
        char_pool += string.digits
        mandatory_chars.append(random.choice(string.digits))
    if use_special:
        char_pool += string.punctuation
        mandatory_chars.append(random.choice(string.punctuation))
        
    # 3. Fill the remaining length with random selections from the pool
    remaining_length = length - len(mandatory_chars)
    password_list = mandatory_chars + [random.choice(char_pool) for _ in range(remaining_length)]
    
    # 4. Shuffle the list to mix the mandatory characters evenly
    random.shuffle(password_list)
    
    return "".join(password_list)

def check_strength(length, use_upper, use_digits, use_special):
    # Basic strength scoring algorithm
    score = 0
    if length >= 12: score += 2
    elif length >= 8: score += 1
    
    if use_upper: score += 1
    if use_digits: score += 1
    if use_special: score += 1
    
    if score >= 5: return "🟢 Strong (Excellent security)"
    if score >= 3: return "🟡 Medium (Good, but could be better)"
    return "🔴 Weak (Highly vulnerable!)"

def password_challenge():
    print("🔐 Welcome to the Random Password Generator Challenge! 🔐\n")
    
    # Get user choices with error protection
    try:
        length = int(input("Enter desired password length (minimum 4): "))
        if length < 4:
            print("❌ Length too short! Defaulting to 12 characters.")
            length = 12
    except ValueError:
        print("❌ Invalid input! Defaulting to 12 characters.")
        length = 12

    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special symbols (e.g., @, #, $)? (y/n): ").strip().lower() == 'y'

    # Generate and test the string
    generated_pwd = generate_password(length, use_upper, use_digits, use_special)
    strength_rating = check_strength(length, use_upper, use_digits, use_special)
    
    print("\n" + "="*45)
    print("🔒 YOUR SECURE PASSWORD LAYER OUTPUT")
    print("="*45)
    print(f"👉 Password: {generated_pwd}")
    print(f"💪 Strength: {strength_rating}")
    print("="*45)

if __name__ == "__main__":
    password_challenge()
