    junior_uniform = [["[1] UNISEX Jersey", 92.00], ["[2] UNISEX PE Shorts", 34.00], ["[3] UNISEX Whanau Tee", 40.00], ["[4] BOYS Short Slevee Shirt", 47.00], ["[5] BOYS Shorts", 55.00], ["[6] BOYS Socks", 9.00], ["[7] GIRLS Short Sleeve Blouse", 46.00], ["[8] GIRLS Skirt", 100.00], ["[9] GIRLS Socks", 9.00]]
    senior_uniform = [["[1] UNISEX Jersey", 92.00], ["[2] BOYS Short Slevee Shirt", 47.00], ["[3] BOYS Tie", 25.00], ["[4] BOYS Trousers", 68.00], ["[5] BOYS Dress Socks", 9.00], ["[6] GIRLS Short Sleeve Blouse", 46.00], ["[7] GIRLS Skirt", 100.00], ["[8] GIRLS Socks", 9.00]]

cart  = []
price = 0
while True:

    option1 = input("Please choose an option from 1 to 4:\n 1. Place Order \n 2. View your Cart \n 3. Purchase \n 4. Exit \n")
    if option1 == "2":
        print(cart)
        print("You are now returning the main menu.")  
    if option1 == "1":
        option = input("Please select whether you want to purchase from the Junior [1] or Senior Uniform [2].")
        
        if option == "1":
            jun_sen = 1
            for name, size in junior_uniform:
                print(f"{name:<30}{size}")

            purchase = input("Please choose a piece of clothing you want to add to the cart between 1 and 9.")
            if purchase == "1":
                option = input('Do you want to add UNISEX Jersey to the cart?, Yes [1] - No [2]')
                if option =="1":
                    print('Added to Cart')
                    cart.append('UNISEX JERSEY')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to main menu.")
            
            elif purchase == "2":
                peshorts = input("Do you want to add UNISEX Pe Shorts to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('UNISEX PE Shorts')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")
            
            if purchase == "3":
                option = input("Do you want to add UNISEX Whanua Tee to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('UNISEX Whanua Tee')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")
                    
            if purchase == "4":
                option = input("Do you want to add BOYS Short Slevee Shirt to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('UNISEX BOYS Short Slevee Shirt')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")
                    
            if purchase == "5":
                option = input("Do you want to add BOYS Shorts to the cart ?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('UNISEX BOYS Shorts')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")
         
            if purchase == "6":
                option = input("Do you want to add BOYS Socks to the cart ?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('UNISEX BOYS Socks')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")
        
            if purchase == "7":
                option = input("Do you want to add GIRLS Short Sleeve Blouse to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('GIRLS Short Sleeve Blouse')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")  
                    
            if purchase == "8":
                option = input("Do you want to add GIRLS Skirt to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('GIRLS Skirt')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu") 
                    
            if purchase == "9":
                option = input("Do you want to add GIRLS SOCKS to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('GIRLS Socks')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")
                   
        if option == "2":
            jun_sen = 2
            for name, size in senior_uniform:
                print(f"{name:<30}{size}")
                
            purchase = input("Please choose a piece of clothing you want to add to the cart between 1 and 8.")
            if purchase == "1":
                option = input('Do you want to add UNISEX Jersey to the cart?, Yes [1] - No [2]')
                if option =="1":
                    print('Added to Cart')
                    cart.append(senior_uniform[int(purchase)-1])
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to main menu.")
                    
            elif purchase == "2":
                peshorts = input("Do you want to add BOYS Short Slevee Shirt to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('BOYS Short Slevee Shirt')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")
            
            if purchase == "3":
                option = input("Do you want to add BOYS Tie to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('BOYS Tie')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")
                    
            if purchase == "4":
                option = input("Do you want to add BOYS Trousers to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('BOYS Trouserst')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")
                    
            if purchase == "5":
                option = input("Do you want to add BOYS Dress Socks to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('BOYS Dress Socks')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")
         
            if purchase == "6":
                option = input("Do you want to add GIRLS Short Sleeve Blouse to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('GIRLS Short Sleeve Blouse')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu")
        
            if purchase == "7":
                option = input("Do you want to add GIRLS Skirt to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('GIRLS Short Sleeve Blouse')
                    print("Returning to Main Menu")
                    
                if option == "2":
                    print("Returning to Main Menu")  
                    
            if purchase == "8":
                option = input("Do you want to add GIRLS Socks to the cart?, Yes [1] - No [2]")
                if option == "1":
                    print("Added to Cart")
                    cart.append('GIRLS Socks')
                    print("Returning to Main Menu")
                if option == "2":
                    print("Returning to Main Menu") 
    
    if option1 == "4":
        print("You are now leaving the application.")
        exit()
    
    if option1 == "3" and jun_sen == 1:
        price = price + junior_uniform[int(purchase)-1][1]
        junior_uniform[int(purchase)-1][1]
        option = input(f'Are you sure you want to purchase {cart}? for {price}. Yes 1 - No 2')
        if option =="1":
            option = input(f'{cart} has been purchased')
        if option == "2":
            print("Returning to main menu.")

    elif option1 == "3" and jun_sen == 2:
        price = price + senior_uniform[int(purchase)-1][1]
        option = input(f'Are you sure you want to purchase {cart}? for {price}. Yes 1 - No 2')
        if option =="1":
            option = input(f'{cart} has been purchased')
        if option == "2":
            print("Returning to main menu.")
