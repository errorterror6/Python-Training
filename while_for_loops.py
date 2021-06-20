
#while(condition is true):
    #indented will loop
b = int(input("Enter a number: "))
a = 0
while a < b:   #this will repeat until the condition is no longer true
    print(a)
    a += 1
    if a == 8:    #you don't need a break, but you can use a break to get out of a loop
        break

print("""

---for loops---

   """)

numbers = [1,2,3,4,5]
a = 1

for a in numbers:
    print(10*a)
    
print("""   

--- maps ---

   """)
#Loops are often used to proccess every item in a list. e.g.
#lets see if all strings in this list are numerical, using the default 
#python function str.isnumeric
numbers_2 = ["1","2","3","4","5","6"]

#we could use:
b = 0
number_length = len(numbers_2)

while b < number_length:
    if str.isnumeric(numbers_2[b]):
        print("Your string " + numbers_2[b] + " is numeric")
    else:
        print("illegal string")
    b += 1

#instead, we can map:
#map(function,list)
#basically applies the function to every member of the list.
#this is very useful if your looping is very complex or long.

if map(str.isnumeric,numbers_2) == False:
    print("my string is illegal")
else:
    print("legal string")



