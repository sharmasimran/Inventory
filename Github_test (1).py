# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:52:21 2020
"""

#Inventory and warehouse management

#Sample case
demand = {'apple':3}
total_demand = 0
for values in demand.values():
    total_demand += values
test_string = "GFG"
Fruit_exists = False
#output_dict  = {}
output_dict_final ={}
supply_warehouse = [{'name':'owd', 'inventory': {'apple': 1}}]
temp_list = []
for key,quantity_input in demand.items():
    for warehouse in supply_warehouse:
        for name,values in warehouse.items():
            if name == 'inventory':
                output_dict  = {}
                temp = warehouse[name] #Store the supply items in a temp variable
                for fruit,warehouse_quantity in temp.items():
                    print(fruit)
                    if key == fruit:
                       # print(quantity_input)
                        #print(warehouse_quantity)
                        if warehouse_quantity >= quantity_input:
                            #print("cond1")
                            output_dict[fruit] = quantity_input
                            cart = warehouse_quantity - quantity_input
                            temp_list.append(output_dict)
                        else:
                           # print("cond2")
                            output_dict[fruit] = warehouse_quantity
                            cart = quantity_input - warehouse_quantity
                            temp_list.append(output_dict)
                        
    
                        #print("items in bag",output_dict)
                        quantity_input = cart
                        demand[fruit] = quantity_input
                       # print(demand[fruit])
                        
           
            
            
                

i = 0
for warehouse in supply_warehouse:
    for values in warehouse.values():
        res = type(values) == str
        if res == True:
            output_dict_final[values] = temp_list[i]
            i+=1
#Validating the cart
cart_items = []
for items in output_dict_final.values():
    cart_items.append(items)
    
cart_sum  = 0
for i in cart_items:
    for q in i.values():
        cart_sum = cart_sum + q

if cart_sum != total_demand:
    output_dict_final = []
print(output_dict_final)
