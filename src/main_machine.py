import coffee_menu as cmenu
import coffee_machine as cm
import coffee_database as db
import time

if __name__ == "__main__":   
    customer = cm.Customer(500)    
    coffee_machine = cm.CoffeeMachine(customer.cash)
    menu = cmenu.CoffeeMenu()
    total_coin = 0
    return_coin = 0
    
    def ask_coin():
        global total_coin        
        main_coin = coffee_machine.coin_input()        
        customer.cash -= main_coin
        total_coin += main_coin
        print(f"Total coins: {total_coin}")


    def ask_coffee():
        global total_coin, return_coin
        main_choice = coffee_machine.coffee_choice()        
        menu.coffee_io(main_choice,total_coin)
        if menu.is_low() == True:
            print("Not enough resources to make the coffee!")
            exit()
        else:        
            price = menu.prices(main_choice)
            return_coin = total_coin - price

        print("Coffee is on the way. Please wait!")
        time.sleep(3)
        print("Coffee is ready!")
        choice = 1
        while choice != 0:
            choice = int(input("Press 0: "))
            if choice != 0:
                print("Invalid input")
        if choice == 0:        
            ask_again()

    def ask_again():
        global return_coin
        print(f"Your return is {return_coin}")
        if return_coin < 50:
            ask_coin()
        else:
            choice = ' '
            while choice not in ['C', 'R']:
                choice = input("Would you like your return or another coffee?(R- return, C - coffee) ").upper()
                if choice not in ['C', 'R']:
                    print("Invalid input!")
            if choice == 'C':
                ask_coffee()
            else:
                print(f"Here is your return ---> {return_coin}")
        

    def main():
        coin_input = True
        while coin_input:
            ask_coin()
            ch = ' '
            while ch not in ['C','M']:
                ch = input("Get coffee or enter coin? (M: coin, C: coffee): ").upper()
                if ch not in ['C','M']:
                    print("Invalid input!")
            if ch == 'M':            
                coin_input = True

            else:
                ask_coffee()
                coin_input = False
            

    main()    