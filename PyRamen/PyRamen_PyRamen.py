# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('(base) fva@Vals-MBP-2 pyramen % /menu_data.csv')
sales_filepath = Path('(base) fva@Vals-MBP-2 pyramen % /sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open(menu_filepath, 'r') as csv_file:
    csv_reader_menu = csv.reader(csv_file)
    #menu = list(csv_reader)
    
    next(csv_reader_menu)
    
    for row in csv_reader_menu:
        item = row[0]
        category = row[1]
        description = row[2]
        price = float(row[3])
        cost = int(row[4])
        
        if category == "entree":
            menu_item_list = [item, category, description, price, cost]
            menu.append(menu_item_list)

# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as csv_file:
    csv_reader_sales = csv.reader(csv_file)
    #sales = list(csv_reader)
    
    next(csv_reader_sales)
    
    for row in csv_reader_sales:
        item_id = int(row[0])
        sale_date = row[1]
        credit_card_number = row[2]
        sale_quantity = int(row[3])
        sale_menu_item = row[4]
        
        sales_row_list = [item_id, sale_date, credit_card_number, sale_quantity, sale_menu_item]
        #print(sales_row_list)
        sales.append(sales_row_list)
        
# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object



    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit








    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
