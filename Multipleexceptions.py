try:
    # Code that might raise different errors
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number

except ValueError:
    # Executes only if the input cannot be converted to an integer
    print("Error: Please enter a valid number, not text.")

except ZeroDivisionError:
    # Executes only if the user inputs 0
    print("Error: You cannot divide by zero.")

except Exception as generic_error:
    # Catch-all fallback for any other unexpected exception
    print(f"An unexpected error occurred: {generic_error}")
