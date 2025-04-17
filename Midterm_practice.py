'''
num =[]
for i in range (5):
    number = int(input("Enter a number: "))
    num.append(number)

even=0
for number in num:
    if number%2==0:
        even = even+1

print (f"there were {even} even numbers")

#Reverse a string
string = input("Enter a word: ").strip()
for i in range(len(string)-1,-1,-1):
    print(string[i])
'''
'''
#Positives and Negatives
positive = 0
negative= 0

nums =[]

for i in range (6):
    number = int(input("Enter a number: "))
    nums.append(number)

for number in nums:
    if number>0:
        positive +=1
    elif number<0:
        negative +=1

print(f"There are {positive} positive numbers.")
print(f"There are {negative} negative numbers.")

#Replace Vowels in a String
string = input("Enter a sentence: ").strip()
for letter in string:
    if letter.lower() == "a" or letter.lower() =="e" or letter.lower() =="i" or letter.lower() =="o" or letter.lower() =="u":
        string = string.replace(letter, "*")
print (string)
'''

#Middle Numbers
nums = []
for i in range (5):
    num = int(input("Enter a number:"))
    nums.append(num)

middle = []
for number in range(1,4):
    middle.append(nums[number])

print (middle)