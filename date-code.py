from datetime import date

# get custom date
d = date(2022, 12, 25)
print("Custom date:", d)

# today() to get current date
todays_date = date.today()
print("Today's date =", todays_date)

# fromtimestamp() to get date from timestamp
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

# get year, month, day using date object
today = date.today() 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)