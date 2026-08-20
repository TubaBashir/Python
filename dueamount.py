def calculate_due_amount():
    try:
        # Request numeric inputs from the user
        total_bill = float(input("Enter the total bill amount: $"))
        amount_paid = float(input("Enter the amount paid so far: $"))
        
        # Calculate the remaining balance
        due_amount = total_bill - amount_paid
        
        # Print results based on payment status
        if due_amount > 0:
            print(f"Remaining balance due: ${due_amount:.2f}")
        elif due_amount == 0:
            print("Bill is fully paid. No amount due!")
        else:
            # If the user overpaid, convert the negative due amount to a positive change value
            print(f"Overpaid! Change to return: ${abs(due_amount):.2f}")
            
    except ValueError:
        print("Invalid input! Please enter numbers only.")

# Run the function
calculate_due_amount()
