import datetime

# Create a date object:
# datetime.datetime()

now_time = datetime.datetime.now()

print(now_time)

print(now_time.year)

# strftime() - method for formatting date objects into readable strings.
print(now_time.strftime("%Y"))
