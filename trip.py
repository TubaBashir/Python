def trip_expense_tracker():
    print("✈️ Welcome to the Trip Expense Tracker ✈️\n")
    
    # Initialize expense categories
    expenses = {
        "Transport (Flights/Train/Gas)": 0.0,
        "Lodging (Hotel/Airbnb)": 0.0,
        "Food & Drinks": 0.0,
        "Activities & Sightseeing": 0.0,
        "Miscellaneous/Shopping": 0.0
    }
    
    # Loop through each category to get input
    for category in expenses:
        while True:
            try:
                cost = float(input(f"Enter total cost for {category}: $"))
                if cost < 0:
                    print("Cost cannot be negative. Please enter a valid amount.")
                    continue
                expenses[category] = cost
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    # Calculate total expenditure
    total_cost = sum(expenses.values())
    
    # Print the financial summary report
    print("\n" + "="*35)
    print("       TRIP EXPENDITURE REPORT      ")
    print("="*35)
    
    if total_cost == 0:
        print("Total Expenses: $0.00 (No expenses recorded)")
        return

    for category, amount in expenses.items():
        percentage = (amount / total_cost) * 100
        print(f"🔹 {category}: ${amount:,.2f} ({percentage:.1f}%)")
        
    print("-" * 35)
    print(f"💰 TOTAL TRIP COST: ${total_cost:,.2f}")
    print("="*35)

if __name__ == "__main__":
    trip_expense_tracker()
