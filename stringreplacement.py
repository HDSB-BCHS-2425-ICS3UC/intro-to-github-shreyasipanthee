# feb 27 2025
#Description: A program that takes in a users first and last name as one string and splits that strinf into a 2 element list. 
#Replaces their last name with *** and prints the new strinf out with the first name and *** replacing their last name.
First_last_name = input("Enter your first and last name: ")
First_last_name = First_last_name.strip()
list = First_last_name.split(" ")
last_name = list[1]
last_name = "*" * len(list[-1])
print(list[0] + " " + last_name)