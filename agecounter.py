from datetime import date

# 1. Get user input
birth_year = int(input("Enter birth year (e.g., 1995): "))
birth_month = int(input("Enter birth month (1-12): "))
birth_day = int(input("Enter birth day (1-31): "))

# 2. Create date objects
birth_date = date(birth_year, birth_month, birth_day)
today = date.today()

# 3. Calculate age
# The boolean check evaluates to 1 if today is before the birthday, subtracting a year
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

print(f"\n You are {age} years old.")
