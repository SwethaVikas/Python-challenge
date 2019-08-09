import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources','budget_data.csv')

# Initialize variables
total_months = []
total_Profit_Losses= []
Monthly_Diff = []
Monthly_PL = []
average_Profit_Losses = 0
Max_increase_profits_date = 0
Max_increase_profits_amount = 0
Max_decrease_losses_date = 0
Max_decrease_losses_amount = 0
Inital_value = 0
Final_value = 0
Date = []

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
        Final_value = int(i(1))
        Monthly_Diff = Final_value - Inital_value
        Monthly_PL.append(Monthly_Diff)
        Inital_value = Final_value
        Max_increase_profits_amount = max(Monthly_PL)
        Max_increase_profits_date = Date[Monthly_PL.index(Max_increase_profits_amount)]

        # Greatest decrease in losses (date and amount) over the entire period
        Max_decrease_losses_amount = min(Monthly_PL)
        Max_decrease_losses_date = Date[Monthly_PL.index(Max_decrease_losses_amount)]

        # Display Result
        print("Financial Analysis") 
        print("--------------------------------")
        print("Total Months" + total_months)
        print("Total" + total_Profit_Losses)
        print("Average" +average_Profit_Losses )  
        print("Greatest Increase in Profits" + Max_increase_profits_date + Max_increase_profits_amount )
        print("Greatest Decrease in Profits" + Max_decrease_losses_date + Max_decrease_losses_amount) 






        




        






