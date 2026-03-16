# 1. Date and Time in Python

# - Python provides the datetime module to work with date and time.
import datetime

now = datetime.datetime.now()  # Get the current date and time
print(now)

today = datetime.date.today() # Getting current date
print(today)

time = datetime.datetime.now().time()  
print(time)

d = datetime.datetime(2020,5,15)
print(d)

#  Formatting Date and Time

# The strftime() function is used to format date and time
now = datetime.datetime.now()

print(now.strftime("%d"))
print(now.strftime("%m"))
print(now.strftime("%Y"))
print(now.strftime("%H:%M:%S"))


# Calander in python

import calendar
print(calendar.calendar(2023)) # print calendar of the year of 2023
print(calendar.month(2005,1)) # print calender of  the month of jan 2005
print(calendar.isleap(2024)) # print if the year 2024 is a leap year or not
print(calendar.weekday(2023, 10, 4)) # print the week of the weekday of the 4 oct 2023
print(calendar.leapdays(2000, 2025)) # print the no of leap year b/w 2000 and 2025

