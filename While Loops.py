#March 24 2025

#Program that asks user for age and if their age is less than 65 it will keeps asking user for their age.
#Ask user for their age
user_age = int(input("Please enter your age: "))

#Keeps asking if that age is below 65
while user_age < 65:
    user_age = int(input("Please enter your age: "))

#Program that will have a variable called num that equals "2" and a second variable called num_2 that has a value of "3".

num_1 = 2
num_2 = 3

while num_2 <= 36:
    num_2 = num_2 * num_1 - num_1
    num_1 = num_1 + 1

print(num_1)
print(num_2)
