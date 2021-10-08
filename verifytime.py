#!/usr/bin/env python

# Brooke Higgins
# CSC119801 Intro to Programming (Python)
# 10/07/2021
# Program that converts standard time to military time

def main():
   #User inputs standard time hour
    hour= int(input("Enter the hour: "))
    if hour >= 1 and hour <= 12 :
       #User inputs "am" or "pm" to calculate military time
       suffix = input("Enter the suffix (am, pm): ")
       suffix = suffix.lower()
       if suffix == "pm" and hour == 12:
          hour = 12
          print(hour)
       elif suffix == "pm" and hour <= 12:
          #Military time is the pm hour + 12, which is calculated here
          hour = hour + 12
          print(hour)
       elif suffix == "am" and hour == 12:
          print("0")
       elif suffix == "am":
          print(hour)
       else :
          #Error messages if either user input is wrong
          print("Error: The suffix must be am or pm.")
    else :
       print("Error: The hour must be between 1 and 12.")
main()