#April 8th 2025
#Testing Lists
'''
class_list = [1 , 5 , 7 , 9]
hello = ["hello", "hello world"]
print (class_list[3])
print(hello[1])
'''

def safe_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0<value<4:
                return value
            else:
                print("Please enter a valid place or index.")
        except ValueError:
            print("Please enter a valid number.")

#Get a user to input an index and print out the list element at that index.
class_list = ["Element 1 at index 0", "Element 2 at index 1", "Element 3 at index 2" ]
index = safe_int_input("Enter the index of a list: ")
print(class_list[index])

#Get a user to input a number for an item on a list (not their index but their place)
place = safe_int_input("Enter the place of an element of a list: ")
print(class_list[place-1])
