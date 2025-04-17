#March 24 2025

#The Nim Problem
import random
print("The game Nim starts out with seven sticks on the table.")
print("Each player takes turns picking up 1, 2 or 3 sticks and cannot pass.")
print("Whoever picks up the last stick loses (the other player wins).")
num_stick = 7

first_second = int(input("Enter 1 if you want to go first. Enter 2 if you want to go second: "))
if first_second == 1:
    print("You go first.")
    user_stick = int(input("Enter the number of sticks you are picking up: "))
    num_stick = num_stick - user_stick

else: 
    print("Computer goes first.")
    num_stick = num_stick - 2

while num_stick > 0:
    pick = int(input(f"There are {num_stick} sticks left. How many sticks do you want to pick? "))
    num_stick = num_stick - pick

    #Computer's pick
    if num_stick > 4:
        comp_pick = random.randint(1,3)
        num_stick = num_stick - comp_pick
    elif num_stick > 3:
        comp_pick = random.randint(1,2)
        num_stick = num_stick - comp_pick
    else:
        comp_pick = 1
        num_stick = num_stick - comp_pick
