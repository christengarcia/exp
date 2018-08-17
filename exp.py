#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# prompt user for the number of items to be recorded
items = input("How many items do you wish to record? ")
items = int(items)


# loop through items
number_of_items = 0

while number_of_items < items:
    print('\n')    
    print("Item " + str(number_of_items + 1))
    
    while True:
        item_cost = input("Please enter the cost for this item: ")
        try:
            item_cost = float(item_cost)
            if item_cost < 0:
                print("Please enter a positive number")
                continue
            break
        except:
            print("Please enter a real number")
            
    while True:
        items_used = input("How many items used? ")
        try:
            items_used = int(items_used)
            if items_used < 0:
                print("Please enter a positive number")
                continue
            break
        except:
            print("Please enter an integer")
            
    tax_deductable = None  
    
    while tax_deductable not in ("Yes", "No"):       
        tax_deductable = input("Is this item tax deductible (Yes|No)? ")
        if tax_deductable == "Yes":
            break
        elif tax_deductable == "No":
            break
        else:
            print("Please enter a Yes or No only")
       
    number_of_items = number_of_items + 1
    
    if number_of_items == items:
        break
    