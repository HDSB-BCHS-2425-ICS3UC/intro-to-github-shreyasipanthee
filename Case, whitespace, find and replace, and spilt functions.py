#Feb 27,2025
'''greeting = "Greetings to you"
name = input ("please enter your name: ")
greeting = greeting + " " + name #Concatenation of strings
print(greeting)#Prints greeting variable to screen'''

message = "heLlO WoRlD"
print(message.capitalize())#Capitalizes the first letter of the first word
print(message.upper())#Capitalizes the entire string
print(message.lower())#Converts all characters in string to lowercase
print(message.title())#Capitalizes the first letter of each word in the string
print(message.swapcase())#Swaps the cases of each letter in the string

#Feb,27,2025 class assignment
#Quote strip functions
quote = "    This is a string   "
print(quote.strip())
print(quote.lstrip())
print(quote.rstrip())

string = str(input("Enter a message "))
nowhitespace = (string.rstrip())
lower = (string.lower())
print (nowhitespace + ".")
print (lower)

#Find and replacing words in strings (find and replace function)
message = "Hello Hello"
print (message)
message= message.replace("Hello", "Goodbye")#Replaces first word with the second
print (message)

print(message.find("Goodbye"))#Prints position of first goodbye
print(message.rfind("Goodbye"))#Prints position of second goodbye

#Split function
message_list = message.split(" ")
print(message_list)
print(message_list[1]) #prints only the second word
