import calendar
#get the input from the user
date_input = input(" Enter the date (MM/DD/YYYY) : ")
month,day,year = map(int,date_input.split())
#Find the date of the week
day_of_week = calendar.weekday(year  ,month , day)
days = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(days[day_of_week])


"""import calendar

# Get the input from the user
date_input = input("Enter the date (MM DD YYYY): ")
month, day, year = map(int, date_input.split())

# Find the day of the week
day_of_week = calendar.weekday(year, month, day)

# List of days in capital letters
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

# Output the correct day
print(days[day_of_week])
"""