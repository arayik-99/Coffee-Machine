import coffee_database as cd
import coffee_machine as cm





class CoffeeMenu:

    
    coffee = cd.component_quantity[0][1]
    sugar = cd.component_quantity[1][1]
    water = cd.component_quantity[2][1]
    
    
    def prices(self,n):
        if n==1:
            return cd.price1
        elif n==2:
            return cd.price2
        elif n==3:
            return cd.price3
        elif n==4:
            return cd.price4
        elif n==5:
            return cd.price5
        elif n==6:
            return cd.price6
        elif n==7:
            return cd.price7
        elif n==8:
            return cd.price8
        elif n==9:
            return cd.price9
        elif n==10:
            return cd.price10

    def coffee_io(self,choice,total):
        
        if choice == 1:            
            with cd.conn:
                self.coffee -= cd.pr1_coffee
                self.sugar -= cd.pr1_sugar
                self.water -= cd.pr1_water
                cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'coffee'",{'value': self.coffee})
                cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'sugar'",{'value': self.sugar})
                cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'water'",{'value': self.water})


        elif choice == 2:
            if total < cd.price2:
                print("Your chosen product's value exceeds your entered coin's value!")
                exit()
            else:
                with cd.conn:
                    self.coffee -= cd.pr2_coffee
                    self.sugar -= cd.pr2_sugar
                    self.water -= cd.pr2_water
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'coffee'",{'value': self.coffee})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'sugar'",{'value': self.sugar})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'water'",{'value': self.water})

        elif choice == 3:
            if total < cd.price3:
                print("Your chosen product's value exceeds your entered coin's value!")
                exit()
            else:
                with cd.conn:
                    self.coffee -= cd.pr3_coffee
                    self.sugar -= cd.pr3_sugar
                    self.water -= cd.pr3_water
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'coffee'",{'value': self.coffee})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'sugar'",{'value': self.sugar})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'water'",{'value': self.water})

        elif choice == 4:
            if total < cd.price4:
                print("Your chosen product's value exceeds your entered coin's value!")
                exit()
            else:
                with cd.conn:
                    self.coffee -= cd.pr4_coffee
                    self.sugar -= cd.pr4_sugar
                    self.water -= cd.pr4_water
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'coffee'",{'value': self.coffee})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'sugar'",{'value': self.sugar})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'water'",{'value': self.water})

        elif choice == 5:
            if total < cd.price2:
                print("Your chosen product's value exceeds your entered coin's value!")
                exit()
            
            else:
            
                with cd.conn:
                    self.coffee -= cd.pr5_coffee
                    self.sugar -= cd.pr5_sugar
                    self.water -= cd.pr5_water
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'coffee'",{'value': self.coffee})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'sugar'",{'value': self.sugar})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'water'",{'value': self.water})

        elif choice == 6:
            if total < cd.price6:
                print("Your chosen product's value exceeds your entered coin's value!")
                exit()
            else:
                with cd.conn:
                    self.coffee -= cd.pr6_coffee
                    self.sugar -= cd.pr6_sugar
                    self.water -= cd.pr6_water
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'coffee'",{'value': self.coffee})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'sugar'",{'value': self.sugar})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'water'",{'value': self.water})

        
        elif choice == 7:
            if total < cd.price7:
                print("Your chosen product's value exceeds your entered coin's value!")
                exit()
            else:
                with cd.conn:
                    self.coffee -= cd.pr7_coffee
                    self.sugar -= cd.pr7_sugar
                    self.water -= cd.pr7_water
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'coffee'",{'value': self.coffee})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'sugar'",{'value': self.sugar})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'water'",{'value': self.water})

        elif choice == 8:
            if total < cd.price8:
                print("Your chosen product's value exceeds your entered coin's value!")
                exit()
            else:
                with cd.conn:
                    self.coffee -= cd.pr8_coffee
                    self.sugar -= cd.pr8_sugar
                    self.water -= cd.pr8_water
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'coffee'",{'value': self.coffee})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'sugar'",{'value': self.sugar})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'water'",{'value': self.water})

        elif choice == 9:
            if total < cd.price9:
                print("Your chosen product's value exceeds your entered coin's value!")
                exit()
            else:
                with cd.conn:
                    self.coffee -= cd.pr9_coffee
                    self.sugar -= cd.pr9_sugar
                    self.water -= cd.pr9_water
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'coffee'",{'value': self.coffee})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'sugar'",{'value': self.sugar})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'water'",{'value': self.water})

        elif choice == 10:
            if total < cd.price10:
                print("Your chosen product's value exceeds your entered coin's value!")
                exit()
            else:

                with cd.conn:
                    self.coffee -= cd.pr10_coffee
                    self.sugar -= cd.pr10_sugar
                    self.water -= cd.pr10_water
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'coffee'",{'value': self.coffee})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'sugar'",{'value': self.sugar})
                    cd.c.execute("UPDATE coffee_components SET quantity = :value WHERE component = 'water'",{'value': self.water})


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



































