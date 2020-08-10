import coffee_database as cd
import coffee_machine as cm


class CoffeeMenu:
   
    def prices(self,n):        
        return cd.price_list[n-1]

    def database_update(self,choice):
        self.updated_list = []     
        self.coffee_prod = []
        for ingr in cd.coffees_dict[choice]:
            self.coffee_prod.append(ingr)
        for item,values in zip(cd.quantity,self.coffee_prod):
            item -= values
            self.updated_list.append(item)
        with cd.conn:
            for updated_item,comp_name in zip(self.updated_list,cd.name):
                cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = :component",{'value': updated_item , 'component': str(comp_name)})




    def coffee_io(self,choice,total):        
        if total < cd.price_list[choice - 1]:
            print("Your chosen product's value exceeds your entered coin's value!")
            exit()
        else:
            self.database_update(choice)


    def is_low(self):
        for init_ingr,product in zip(cd.quantity,self.coffee_prod):
            if product > init_ingr:
                return True
        return False