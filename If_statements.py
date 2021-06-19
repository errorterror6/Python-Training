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

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(4,5,6))