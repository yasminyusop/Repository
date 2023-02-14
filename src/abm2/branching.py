# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:10:40 2023

@author: gy22fybm
"""


# A simple If Statement
day_of_week = 5
day = "Weekday"
if day_of_week >= 6:
    day = "Weekend"
# An If-else Statement
if day_of_week < 6:
    day = "Weekday"
else:
    day = "Weekend"
# An If-elif Statement
if day_of_week == 1:
    day = "Monday"
elif day_of_week == 2:
    day = "Tuesday"
elif day_of_week == 3:
    day = "Wednesday"
elif day_of_week == 4:
    day = "Thursday"
elif day_of_week == 5:
    day = "Friday"
else:
    day = "Weekend"
    
day_of_week = 5
match day_of_week:
    case 1:
        day = "Monday"
    case 2:
        day = "Tuesday"
    case 3:
        day = "Wednesday"
    case 4:
        day = "Thursday"
    case 5:
        day = "Friday"
    case _:
        day = "Weekend"    