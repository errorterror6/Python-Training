friends = ["Kevin", "Karen", "Jim"]

print(friends)
print(friends[0])
print(friends[-1])

print(friends[1:])
print(friends[1:2]) #specifies range

friends[1] = "Mike"  #modifying lists.
print(friends[1])  #this gives mike.
print("\n\n ---List Functions--- \n")

#list functions
lucky_numbers = [4,8,15,6,23,42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)  #gives friends followed by lucky numbers

friends.append("Creed") #added function onto the end of the list
print(friends)

friends.insert(1, "Kelly") #puts kelly in position 1
print(friends)

#friends.clear()   clears the list
friends.pop() #removes the last element of the list

print(friends.index("Kevin"))   #tells me if kevin is in the list, and the index.
print(friends.count("Jim"))  #amount of times Jim comes up
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()   #now the list is in alphabetical/numerical ascending order.
lucky_numbers.reverse()  #reverses the order of the list
print(friends)
friends2 = friends.copy()   #copies friends

#tuples
print("\n\n --- Tuples --- \n")
#tuples are unmutable, i.e. they cannot be changed.
coordinates = (4,5)
print(coordinates)
#you can create a list of tuples
coordinates2 = [(4,5), (7,4) , (2,3)]

print("\n\n --- Functions --- \n")

def say_hi (): #all code after this is included in this function. must be indented
    #same as maths function f(x) = y. the input x is a parameter.
    print("Hello user") #this won't get printed. code inside a fn is not executed by default. it needs to be "called"

print("top text")
say_hi()   #this executes the function
print("bottom text")

def sayhi2 (name, age):
    print("hello user " + name + " you are " + age)

sayhi2("Solari", "26")
sayhi2("Lunari", "24")


def cub3(num):
    float(num)*float(num)*float(num)

print(cub3(3)) #this gives none

def cube(num):
    return num*num*num #returns a value back to the caller. gets information back from a fn. you
#cannot put any code after the return (i.e. next line won't show.). return breaks out of the fn.
result = cube(4)
print(result)

