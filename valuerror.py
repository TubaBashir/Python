# Standard pattern to handle a ValueError
try:
    user_input = input("Enter a valid integer: ")
    number = int(user_input)  # This will fail if input is not a number
    print(f"Success! Your number is {number}")

except ValueError as error_message:
    # This block runs only if a ValueError occurs
    print(f"Error encountered: {error_message}")
    print("Please make sure you type digits only (e.g., 42).")
