# Author: Shreya Panthee
# Date modified: 2025-04-17

# Problem 1: Program that prints the smallest number among 5 numbers entered by user.

# Initializing list to store all 5 numbers entered by user
numbers = []

#Loop for user input
for i in range(1,6):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num) #Adds entered number to list

# Variable to store smallest number in list
smallest = numbers[0]

# Loop for checking which number is the smallest
for number in numbers:
    if number < smallest:
        smallest = number

# Display message
print (f"The minimum number is: {smallest}") #displays the smallest number

# Author: Shreya Panthee
# Date modified: 2025-04-17

#Problem 2: Program that prints the number of characters in a given string(including spaces)

# Asks user to enter a sentence and removes whitespace
sentence  = input("Enter a sentence: ").strip()

# Display Message
print(f"The sentence has {len(sentence)} characters.") # Displays number of characters