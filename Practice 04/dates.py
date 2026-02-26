from datetime import datetime, timedelta

# 1. Subtract five days from current date
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Current date:", current_date)
print("5 days ago:", new_date)


# 2. Print yesterday, today, tomorrow
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("\nYesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


# 3. Drop microseconds from datetime
now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("\nWith microseconds:", now)
print("Without microseconds:", without_microseconds)


# 4. Calculate difference between two dates in seconds
date1 = datetime(2025, 6, 1, 12, 0, 0)
date2 = datetime(2025, 6, 2, 12, 0, 0)

difference = date2 - date1
print("\nDifference in seconds:", difference.total_seconds())