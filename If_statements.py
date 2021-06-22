print("Welcome")

is_male = True #boolean
is_tall = False

if is_male == True or is_tall == True:
    print("you are a male or tall or both")   #everything in the indentation will be executed if true.
else:
    print("you are neither male or tall.")

if is_male == True and is_tall == True:
    print("you are a tall male")  # everything in the indentation will be executed if true.
elif is_male and not(is_tall):
    print("you are a short male")
else:
    print("you are either not male or not tall or both.")

