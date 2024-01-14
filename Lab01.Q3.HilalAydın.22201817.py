# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:13:07 2023

@author: hilala-ug
"""

"""
Write a program to input the number of seconds. The program will display the number of days,
number of hours, number of minutes, and seconds, if any, in the input number of seconds. If the
input is not a positive integer, display an appropriate message. Note that there are 60 seconds in a
minute, 60 minutes in an hour and 24 hours in a day. The user input is shown in red.
Sample Run:
Enter number of seconds: -10
The number of seconds must be
positive.
Sample Run:
Enter number of seconds: 10
10 secs
Sample Run:
Enter number of seconds: 100
1 mins 40 secs
Sample Run:
Enter number of seconds: 10000
2 hours 46 mins 40 secs
Sample Run:
Enter number of seconds: 100000
1 days 3 hours 46 mins 40 secs
Sample Run:
Enter number of seconds: 500040
5 days 18 hours 54 mins 0 secs
"""

seconds= int(input("Enter number of seconds: "))


if seconds <= 0 :
    print("The number of seconds must be positive.")
    
if seconds >= 0:
    
    minutes = seconds // 60
    remaining_minutes = minutes % 60 
  
    hours = minutes // 60
    remaining_hours = hours % 24
   
    days = hours // 24 
    
    remaining_secs= seconds % 60
    
    
    if days > 0:
       print(f"{days} days {remaining_hours} hours {remaining_minutes} mins {remaining_secs} secs")
    elif hours > 0:
       print(f"{remaining_hours} hours {remaining_minutes} mins {remaining_secs} secs")
    elif minutes > 0:
       print(f"{remaining_minutes} mins {remaining_secs} secs")
    else:
       print(f"{remaining_secs} secs")