import sqlite3

conn = sqlite3.connect('coffee_main.db')
c = conn.cursor()
with conn:
    c.execute("SELECT * FROM coffee_products")
    coffees = c.fetchall()   
    c.execute("SELECT * FROM coffee_components")
    component_quantity = c.fetchall()


quantity = []
name = []
for comp_name, comp_quant in component_quantity:
    quantity.append(comp_quant)
    name.append(comp_name)

coffees_dict = {}
price_list = []
for c_id, price, coffee, sugar, water in coffees:
    price_list.append(price)
    d = {c_id:(coffee,sugar,water)}
    coffees_dict.update(d)

for i in quantity:
    if i == 0:
        print("Your supplies of coffee/water/sugar has ended.")
        print("Please refill your supplies")
        exit()