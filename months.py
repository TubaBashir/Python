import calendar

# 1. Full month names (starts with an empty string at index 0)
full_months = list(calendar.month_name)[1:]
print("Full Months:", full_months)

# 2. Abbreviated month names (Jan, Feb, Mar...)
short_months = list(calendar.month_abbr)[1:]
print("\nShort Months:", short_months)
