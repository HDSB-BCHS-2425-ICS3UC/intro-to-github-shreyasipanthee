#march 18th 2025

sum = 0
for i in range (0,101):
    sum = sum + i
print(sum)

'''for i in range (0,101,2):
    print(i) #This will print 0,2,4,6,8,10,12......

for i in range (1,101,2):
    print(i) #Prints 1,3,5,7,9,.....

#For loop that will print out all the 2's times tables from 1-11

for i in range (1,12):
    print(2*i)

#For loop that will print a countdown message to a bomb timer
import time

for i in range (11,-1,-1):
    time.sleep(1)#will delay the program for 1 second
    print("Bomb will explode in: " + str(i))
print("Bomb has exploded.")

#Program that will print out a right trieangle od stars. Number of rows according to user input.

rows = int(input("Enter the number of rows of stars you would like to print to make a triangle: "))

for i in range (1,int(rows+1)):
    for k in range (1,i):
        print ("*" * 1)'
        '''

loop = int(input(" Enter the amount of rows that you want: "))

for rows in range (1,(loop+1)/2):
    total = "*" * rows
    print(total)

    if rows>(1002/2):
        for rows in range ((loop)/2 , 1, -1):
            total = rows * "*"
            print (total)