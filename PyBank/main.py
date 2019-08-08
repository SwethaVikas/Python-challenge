import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources','budget_data.csv')

# Initialize variables
total_months = []
total_Profit_Losses= []
Monthly_Diff=[]
average_Profit_Losses = 0
greatest_increase_profits_date = 0
greatest_increase_profits_amount = 0
greatest_decrease_losses_date = 0
greatest_decrease_losses_amount = 0

# with open(budget_data_csv, newline="") as csvfile:
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the Header of the file
    csv_header = next(csvreader)
    for i in csvreader:

        # Counting the total number of months
        total_months.append(i[0])

        # Adding total profit or losses
        total_Profit_Losses.append(i[1])

        # Average of the changes in "Profit/Losses" over the entire period 
        average_Profit_Losses = total_Profit_Losses/total_months

        # Greatest increase in profits date and Amount te over the entire period
        Monthly_Diff = int(i[1])



        






