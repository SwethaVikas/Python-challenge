import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources','budget_data.csv')

# Initialize variables
total_months = 0
total_Profit_Losses= 0
Monthly_Diff = []
Total_monthly_diff = 0
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
        total_months= total_months + 1
        Date.append(i[0])

        # Adding total profit or losses
        total_Profit_Losses = total_Profit_Losses + int(i[1])

        # Greatest increase in profits date and Amount te over the entire period
        
        Final_value = int(i[1])
        Monthly_Diff = Final_value - Inital_value
        Monthly_PL.append(Monthly_Diff)
        

        # Average of the changes in "Profit/Losses" over the entire period 
        Total_monthly_diff = Total_monthly_diff + Monthly_Diff      
        average_Profit_Losses = (Total_monthly_diff/total_months)

        Max_increase_profits_amount = max(Monthly_PL)
        Max_increase_profits_date = Date[Monthly_PL.index(Max_increase_profits_amount)]

        # Greatest decrease in losses (date and amount) over the entire period
        Max_decrease_losses_amount = min(Monthly_PL)
        Max_decrease_losses_date = Date[Monthly_PL.index(Max_decrease_losses_amount)]
        Inital_value = Final_value
    
    
    # Display Result
    print("Financial Analysis") 
    print("--------------------------------")
    print("Total Months " + str(total_months))
    print("Total " + "$"+ str(total_Profit_Losses))
    print("Average " +"$"+ str(int(average_Profit_Losses)))
    print("Greatest Increase in Profits " +str(Max_increase_profits_date) +" $" + str(Max_increase_profits_amount))
    print("Greatest Decrease in Profits "+ str(Max_decrease_losses_date) + " $" + str(Max_decrease_losses_amount)) 






        




        






