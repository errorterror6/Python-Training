#this doc contains strings, numbers, variables, input.

###drawing shapes###
print("drawing shapes")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print("assigning variables")
#assigning variables
character_name = "John"
character_age = "35"
isMale = True
#basic types of data: strings (plain text), numbers, boolean (T/F)
print("There once was a man named " + character_name)
print("He was "+ character_age)
print("\n\n")

#working with strings
print("working with strings\n\n")

print("Giraffe\nAcademy")
#\n inserts a new line.
print("Giraffe\"Academy")
#the backslash renders the character right behind it, such as ".
print("Giraffe/Academy")
#this only prints Giraffe/Academy
print("\n\n")


#some functions
phrase= "Giraffe Academy"
print(phrase.lower()) #converts all to lower case
print(phrase.upper())
print(phrase.isupper()) #checks if it is entirely upper/lower
print(phrase.upper().isupper())
print(len(phrase)) #length function
print(phrase[0]) #grabs the particular character, gives G. strings index starts with 0
print(phrase.index("Acad")) #returns index (8) as thats where it starts. will give error if not found.
print(phrase.replace("Giraffe", "HEEHEEXD"))

print("\n\n")



#NUMBERS

from math import *
#^gives us access to a lot more maths functions.

print("---NUMBERS---\n")

print(3+4.405)
print(3 * 4 + 5)
print(3 * (4+5)) #standard order of operations, and using brackets to change that.
print(10 % 3) #modulo. basically gives the remainder.

print("\n")
my_num = -12
print(my_num * 5)

print(str(my_num)) #converts the number into a string. allows you to print it out along strings
print("my favourite number is " + str(my_num))

print(abs(my_num)) #absolute value
print(pow(5,3)) #5^3
print(min(3,2))
print(max(3,2))
print(round(7.8))
print(floor(7.8))
print(ceil(7.8))

print(sqrt(37))

print("\n\n")

print("inputs \n")



#--- INPUTS ---

#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hello " + name + "! " + age)


#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = num1 + num2 #this is read as strings and 3, 5 will give 35.
#result = int(num1) + int(num2) #this is read as integers and 3, 5 will give 8.
#print(result)

#OR
#result = float(num1) + float(num2) #for decimal places. int can only handle integers.

color = input("Enter a color: ")
plural_noun = input("Enter a Plural noun: ")
Celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + Celebrity)
