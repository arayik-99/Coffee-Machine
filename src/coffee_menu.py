import coffee_database as cd
import coffee_machine as cm


class CoffeeMenu:
   
    def prices(self,n):
        return cd.price[n-1]

    def database_update(self,n):
        self.updated_list = []     
        self.coffee_prod = []
        for ingr in cd.coffees_dict[n]:
            self.coffee_prod.append(ingr)
        for item,values in zip(cd.quantity,coffee_prod):
            item -= values
            self.updated_list.append(item)
        with cd.conn:
            for updated_item,comp_name in zip(updated_list,cd.name):
                cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = :component",{'value': updated_item , 'component': str(comp_name)})




    def coffee_io(self,choice,total):        
        if total < cd.price_list[choice - 1]:
            print("Your chosen product's value exceeds your entered coin's value!")
            exit()
        else:
            database_update(choice)


    def is_low(self,choice):
        if choice == 1:
            if cd.pr1_coffee > cd.coffee or cd.pr2_sugar > cd.sugar or cd.pr2_water > cd.water:
                return True
        elif choice == 2:
            if cd.pr2_coffee > cd.coffee or cd.pr2_sugar > cd.sugar or cd.pr2_water > cd.water:
                return True
        elif choice == 3:
            if cd.pr3_coffee > cd.coffee or cd.pr3_sugar > cd.sugar or cd.pr3_water > cd.water:
                return True
        elif choice == 4:
            if cd.pr4_coffee > cd.coffee or cd.pr4_sugar > cd.sugar or cd.pr4_water > cd.water:
                return True
        elif choice == 5:
            if cd.pr5_coffee > cd.coffee or cd.pr5_sugar > cd.sugar or cd.pr5_water > cd.water:
                return True
        elif choice == 6:
            if cd.pr6_coffee > cd.coffee or cd.pr6_sugar > cd.sugar or cd.pr6_water > cd.water:
                return True
        elif choice == 7:
            if cd.pr7_coffee > cd.coffee or cd.pr7_sugar > cd.sugar or cd.pr7_water > cd.water:
                return True
        elif choice == 8:
            if cd.pr8_coffee > cd.coffee or cd.pr8_sugar > cd.sugar or cd.pr8_water > cd.water:
                return True
        elif choice == 9:
            if cd.pr9_coffee > cd.coffee or cd.pr9_sugar > cd.sugar or cd.pr9_water > cd.water:
                return True
        elif choice == 10:
            if cd.pr10_coffee > cd.coffee or cd.pr10_sugar > cd.sugar or cd.pr10_water > cd.water:
                return True
        
        return False