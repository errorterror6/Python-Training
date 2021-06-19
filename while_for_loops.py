
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

for loops

   """)

numbers = [1,2,3,4,5]
a = 1

for a in numbers:
    print(10*a)


