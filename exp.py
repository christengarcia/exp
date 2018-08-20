#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program that allows the user to choose an unlimited number 
of items to be recorded. It outputs the most expensive item,
average cost per item, total expenses and total tax deductible.
"""

# function to get non-negative float input from user
def get_non_negative_float(prompt):
    try:
        value = float(input(prompt))
    except ValueError:
        print("Please enter a real number.")
        return get_non_negative_float(prompt)
    if value < 0:
        print("Please enter a positive number.")
        return get_non_negative_float(prompt)
    else:
        return value
    
# function to get non-negative integer input from user   
def get_non_negative_int(prompt):
    try:
        value = int(input(prompt))
    except ValueError:
        print("Please enter an integer.")
        return get_non_negative_int(prompt)
    if value < 0:
        print("Please enter a non-negative integer.")
        return get_non_negative_int(prompt)
    else:
        return value
    
# function to apply tax deduction based on user's yes or no response
def tax_deductible(question):
    while "the answer is invalid":
        reply = str(input(question+'(Yes/No): '))
        if reply == "Yes" or reply == "yes":
            tax = item_cost * items_used
            return tax
            break
        if reply == "No" or reply == "no":
            tax = 0
            return tax
            break
        else:
            print("Please enter a Yes or No only. ")            

# prompt user for the number of items to be recorded
items = input("How many items do you wish to record? ")
items = int(items)    

# empty expensive items dictionary, items and tax list
expensive_items_list = {}
items_list = []
tax_list = []

# loop through number of items specified by the user
number_of_items = 0
while number_of_items < items:
    print("------------------------------------------")   
    print("Item " + str(number_of_items + 1) + ":")
    
    # call the functions with arguements and assign to new variable
    item_cost = get_non_negative_float("Please enter the cost for this item: ")   
    items_used = get_non_negative_int("How many items used? ")      
    tax = tax_deductible("Is this item tax deductible? ")
    
    # multiply item cost/used and add result to items or tax list respectively
    total = (item_cost * items_used)
    items_list.append(total)
    tax_list.append(tax) 
    
    # add expensive items with item number to dictionary
    expensive_items_list.update({number_of_items +1: total})
    
    # most expensive item calculation
    maximum = max(expensive_items_list, key=expensive_items_list.get)    
       
    # average cost per item calculation
    average_cost_per_item = sum(items_list)/items
    
    # total expenses calculation
    total_expenses = sum(items_list)
    
    # total tax deductible calculation
    total_tax_deductible = sum(tax_list) 
    
    number_of_items = number_of_items + 1            
    if number_of_items == items:
        break
    
# main method to print results
def main():
    print("+----------------------------------------+")
    print("Most expensive item:    ", '$%.2f' % expensive_items_list[maximum], "  Item:",maximum)
    print("Average cost per item:  ", '$%.2f' % average_cost_per_item)
    print("Total expenses:         ", '$%.2f' % total_expenses)
    print("Total tax deductible:   ", '$%.2f' % total_tax_deductible)    
    print("+----------------------------------------+")
# Execute main() function
if __name__ == '__main__':
    main()

 