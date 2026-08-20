while True:
    user_input = input("Enter a command (type 'exit' to quit): ").strip().lower()
    
    if user_input == "exit":
        print("\n🚪 That's the exit! Goodbye!")
        break  # Safely breaks out of the running loop
        
    print(f"Processing command: '{user_input}'...")
