def calculator():
    while True:
        try:
            choice = input("1(+), 2(-), 3(*), 4(/), 5(Exit): ")
            if choice == '5': break
            if choice not in ('1', '2', '3', '4'): continue
            
            n1 = float(input("First number: "))
            n2 = float(input("Second number: "))
            
            if choice == '1': print(n1 + n2)
            elif choice == '2': print(n1 - n2)
            elif choice == '3': print(n1 * n2)
            elif choice == '4':
                print(n1 / n2 if n2 != 0 else "Error: Div by 0")
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    calculator()
