from datetime import datetime

now = datetime.now()

# Format: DD/MM/YYYY Hour:Minute:Second AM/PM
formatted_1 = now.strftime("%d/%m/%Y %I:%M:%S %p")
print("Format 1:", formatted_1)

# Format: Text-based (e.g., Month Day, Year)
formatted_2 = now.strftime("%B %d, %Y - %H:%M")
print("Format 2:", formatted_2)
