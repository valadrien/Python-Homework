'''Your task is to create a Python script that analyzes the records to calculate each of the following:
The total number of months included in the dataset
The total net amount of "Profit/Losses" over the entire period
The average change in "Profit/Losses" between months over the entire period
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in losses (date and amount) over the entire period
As an example, your analysis should look similar to the one below: 
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''

# Load panda libraries with alias 'pd'
import pandas as pd

# Read data from file 'budget_data.csv'
# in the same directory as the python homework process
data = pd.read_csv("budget_data.csv")
budget_report = data.values.tolist()

# Count The total number of months included in the dataset.
total_months = len(budget_report)

# Print the Net Total Amount of Profit and Loss over the entire over the entire period. 
net_total = data.iloc[:,1].sum()

# The average Profit & Loss Change Rate Over the defined time period
total_amount = budget_report[0][1]
average_sum = 0.00
previous_month = budget_report[0][1]
previous_month_text = budget_report[0][0]
greatest_increase = previous_month
greatest_increase_text = previous_month_text
greatest_loss = 0
greatest_loss_month = previous_month_text

for month in budget_report[1:]:
    current_month_pl = month[1]
    current_month_text = month[0]
    
# Calculate total 
    total_amount += current_month_pl
    
# Getting the averate rate of change
    difference_between_months = current_month_pl - previous_month
    average_sum += difference_between_months
    
    previous_month = current_month_pl
    previous_month_text = current_month_text
    
# Identifying the greatest month profit increase and it's value
    if difference_between_months > greatest_increase:
        greatest_increase = difference_between_months
        greatest_increase_month = current_month_text
    
# Identifying the greatest month profit increase and it's value
    if difference_between_months < greatest_loss:
        greatest_loss = difference_between_months
        greatest_loss_month = current_month_text

# Print Resulsts as illusrated format 😎
print("Financial Analysis")
print("------------------------------------------------------------")
print(f"Net Total P&L is: $ {net_total}")
print(f"The average change rate is: $ {round(average_sum/(total_months-1),2)}")
print(f"Greatest Increase in Profits happened in: {greatest_increase_month} ($ {greatest_increase})")
print(f"Greatest Decrease in Profits happened in: {greatest_loss_month} ($ {greatest_loss})")

