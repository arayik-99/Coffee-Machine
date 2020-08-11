coin_dict = {'50':50,'100':100,'200':200,'500':500}
import coffee_database as cd

class CoffeeMachine:           
    def __init__(self,customer_cash):        
        self.customer_cash = customer_cash        
        if self.customer_cash < 50:
            print("You don't have enough money!")
            exit()       
        else:
            self.start()

    def start(self):
        print('\n')
        print('+-----------------------------+')
        print('|Allowed coins: 50,100,200,500|')     
        print('+-----------------------------+\n')
        print('  +-------------------------+')
        print('  |Coffee machine on standby|')     
        print('  +-------------------------+\n')
        print('+------------------------------+')            
        print("""|Coffee 1:  50 | Coffee 2: 100 |
|--------------+---------------|
|Coffee 3: 150 | Coffee 4: 200 |
|--------------+---------------|
|Coffee 5: 250 | Coffee 6: 300 |
|--------------+---------------|
|Coffee 7: 350 | Coffee 8: 400 |
|--------------+---------------|
|Coffee 9: 450 | Coffee 10: 500|""")
        print('+------------------------------+\n')   
        
                             
    def coin_input(self):        
        self.coin_list = coin_dict.keys()
        self.coin = ' '
        while self.coin not in self.coin_list:
            self.coin = input('Please insert a coin: ')
            if self.coin not in self.coin_list:
                print('Invalid coin!')                
            elif int(self.coin) > self.customer_cash:
                print("You don't have enough resources.")
                exit()        
        return coin_dict[self.coin]
        

    def coffee_choice(self):
        self.choice = ' '
        while self.choice not in cd.coffee_id:
            self.choice = int(input("Choose your coffee: "))
            if self.choice not in cd.coffee_id:
                print('Invalid choice!')
        return int(self.choice)


class Customer:
    def __init__(self,cash):
        self.cash = cash

    def __str__(self):
        return f"I have {self.cash} $"