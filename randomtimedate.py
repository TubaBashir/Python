import random
from datetime import datetime, timedelta

def get_random_datetime(start_date, end_date):
    # 1. Calculate the total time difference between dates
    time_between = end_date - start_date
    seconds_between = int(time_between.total_seconds())
    
    # 2. Pick a random number of seconds within that range
    random_seconds = random.randint(0, seconds_between)
    
    # 3. Add the random seconds to the start date
    return start_date + timedelta(seconds=random_seconds)

# Example: Generate a random date/time between Jan 1, 2020 and Dec 31, 2025
start = datetime(2020, 1, 1, 0, 0, 0)
end = datetime(2025, 12, 31, 23, 59, 59)

random_result = get_random_datetime(start, end)

print("Random Date and Time:", random_result)
print("Formatted:", random_result.strftime("%B %d, %Y at %I:%M %p"))
