import sqlite3

conn = sqlite3.connect('coffee_main.db')
c = conn.cursor()


#                                             REAL    REAL   REAL
#First table's name = coffee_components -->  coffeee, sugar, water


#                                             INTEGER  INTEGER  REAL   REAL   REAL
#Second table's name = coffee_products -->   coffee_id, price, coffee, sugar, water


with conn:
    c.execute("SELECT * FROM coffee_products")
    coffee_list = c.fetchall()
    

with conn: 
    c.execute("SELECT * FROM coffee_components")
    component_quantity = c.fetchall()


# components
coffee = component_quantity[0][1]
sugar = component_quantity[1][1]
water = component_quantity[2][1]


# prices
price1 = coffee_list[0][1]
price2 = coffee_list[1][1]
price3 = coffee_list[2][1]
price4 = coffee_list[3][1]
price5 = coffee_list[4][1]
price6 = coffee_list[5][1]
price7 = coffee_list[6][1]
price8 = coffee_list[7][1]
price9 = coffee_list[8][1]
price10 = coffee_list[9][1]


pr1_coffee,pr1_sugar,pr1_water = coffee_list[0][2],coffee_list[0][3],coffee_list[0][4]
pr2_coffee,pr2_sugar,pr2_water = coffee_list[1][2],coffee_list[1][3],coffee_list[1][4]
pr3_coffee,pr3_sugar,pr3_water = coffee_list[2][2],coffee_list[2][3],coffee_list[2][4]
pr4_coffee,pr4_sugar,pr4_water = coffee_list[3][2],coffee_list[3][3],coffee_list[3][4]
pr5_coffee,pr5_sugar,pr5_water = coffee_list[4][2],coffee_list[4][3],coffee_list[4][4]
pr6_coffee,pr6_sugar,pr6_water = coffee_list[5][2],coffee_list[5][3],coffee_list[5][4]
pr7_coffee,pr7_sugar,pr7_water = coffee_list[6][2],coffee_list[6][3],coffee_list[6][4]
pr8_coffee,pr8_sugar,pr8_water = coffee_list[7][2],coffee_list[7][3],coffee_list[7][4]
pr9_coffee,pr9_sugar,pr9_water = coffee_list[8][2],coffee_list[8][3],coffee_list[8][4]
pr10_coffee,pr10_sugar,pr10_water = coffee_list[9][2],coffee_list[9][3],coffee_list[9][4]









if coffee == 0 or sugar == 0 or water == 0:
    print("Your supplies of coffee/water/sugar has ended.")
    print("Please refill your supplies")
    exit()



    
