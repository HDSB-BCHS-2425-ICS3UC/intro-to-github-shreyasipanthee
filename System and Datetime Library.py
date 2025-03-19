#March 3rd 2025
import sys
import datetime
version = sys.version
info = sys.version_info
print("Python version is " + str(version))
print("Information: " + str(info))

todays_date = datetime.datetime.now()
print (todays_date)
print(str(todays_date.year) + "-" + str(todays_date.month) + "-" + str(todays_date.day))
print(todays_date.month)
