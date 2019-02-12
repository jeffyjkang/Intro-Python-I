"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


thisYear = datetime.now().year
thisMonth = datetime.now().month

print("Welcome to calendar display")
print("Please choose to continue...")
# print("Please choose year 4 digits:")
# userYear = int(input("") or thisYear)
# print("Please choose month:")
# userMonth = int(input("") or thisMonth)

userInput = [int(x)
             for x in input("Please enter the month and year: ").split()]

# print(len(userInput))
if len(userInput) == 0:
    calendarMonth = calendar.month(thisYear, thisMonth)
    print(calendarMonth,
          "\n Please provide Month and Year inputs, month followed by 4 digit year")
elif len(userInput) > 2:
    print("Error please only provide month and 4 digit year")
elif len(userInput) == 1:
    if(userInput[0] > 12 or userInput[0] < 1):
        print("Error! please choose month between the numbers 1 through 12")
    calendarMonth = calendar.month(thisYear, userInput[0])
    print(calendarMonth)
else:
    if(userInput[0] > 12 or userInput[0] < 1):
        print("Error! please choose month between the numbers 1 through 12")
    if(userInput[1] < 0):
        print("Error! year not in range")
    calendarMonth = calendar.month(userInput[1], userInput[0])
    print(calendarMonth)

# while not userYear:
#     print("Please choose year")
# while not userMonth:
#     print("Please choose month")


# calendarMonth = calendar.month(thisYear, thisMonth)
# calendar = calendar.calendar(thisYear, thisMonth)
# dateMonth = datetime(today.month)
# dateMonth = datetime(today.month)

# print(thisYear)
# print(thisMonth)
# calendarMonth = calendar.month(userYear, userMonth)
# print(calendarMonth)
