# Today I am going to Learn about the Strings in Python .


#   Normal Strings

print("Hello ! this is Eashanth sai")

# quotes inside the string

print("Hello This is eashanth's Laptop")
print('Hey this belongs to Eashanth\'s Project ')
print('He asked "How do you do ?"')

# Assign a String to a variable

name = "Eashanth sai"
print(name)

# multi line Strings

multi_line_String = """This is a multi line String. 
We can type entire Paragraph in this String and it will be printed as it is. """
print(multi_line_String)

# String Concatination

First_name = "Eashanth"
Last_name = "sai"
print(First_name + " " + Last_name) # here we are concatinating the two strings and printing it

# String Arrays

name1 = "bunty"
print(name1[0]) # prints the first character of the string
print(name1[1]) # prints the second character of the string
print(name1[2]) # prints the third character of the string
print(name1[3]) # prints the fourth character of the string
print(name1[4]) # prints the fifth character of the string

# Looping  through a String

for x in name1:
    print(x)

# Finding the length of a String 

print(len(name))

# Checking if a certain phrase or character is present in a string

txt = "Hello, boys and girls."

print('girls' in txt)
print('Bunty' not in txt)

if 'girls' in txt:
    print("Yes , girls is present in the String")

#Slicing the Strings
print(name1[1:4])#this is the method uesd to Slice the String in Python it will print the first three characters of the String
print(name1[:5]) # this will print the first five characters of the String
print(name1[1:5]) #in this line we are printing the String from the Second to the Last which means we are slicing the String for the Beginning)
print(name1[-5:-1])# here we are using the negative indexing where we cannot determine the length of the String but we can use this method to Sclie the String


#changng the case of the String
print(name1.upper())#here we are changing the String to Uppercase this is method to modify the CASE of the String
print(name1.lower())#here we are changing the String to Lowercase this is method to modify the CASE of the String

NAME = " Eashanth sai "
print(NAME.strip())# This is a method used to remove the whitespace form the Begining and the END of the String

print(NAME.replace('Eashanth',"Bunty"))# This is a method used to replace the String with another String
