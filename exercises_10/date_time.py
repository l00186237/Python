from datetime import datetime as dt

# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print("Current Time (full):", today)

# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print("Unix Epoch Time:", unix_epoch_time)

# Extract human-readable values
year = today.year
month = today.month
day = today.day
hour = today.hour
minute = today.minute
second = today.second

# Print human-readable values
print(f"Current Date: {year}-{month:02d}-{day:02d}")
print(f"Current Time: {hour:02d}:{minute:02d}:{second:02d}")
