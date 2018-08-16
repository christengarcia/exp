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
    item_cost = input("Please enter the cost for this item: ")
    item_cost = float(item_cost)
    item_used = input('How many of this item were used? ')
    item_used = int(item_used)
    tax_deductable = input("Is this item tax deductible (Yes|No)? ")
    tax_deductable = bool(tax_deductable)
       
    number_of_items = number_of_items + 1
    
    if number_of_items == items:
        break