
import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources','election_data.csv')

#Initialize variables
total_votes = 0
kcount = 0
ccount = 0
lcount = 0
ocount = 0
max_votecount = 0

#Function for % calculation
def percentage (part, whole):
    return 100 * float(part)/float(whole)

with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for i in csvreader:
        voterid = i[0]
        country = i[1]
        candidate = i[2]
        # Find Total Vote Count
        total_votes = total_votes + 1

        # Find votecount by candidates
        if candidate =="Khan":
           kcount = kcount + 1
        if candidate =="Correy":
           ccount = ccount + 1
        if candidate =="Li":
           lcount = lcount + 1
        if candidate =="O'Tooley":
           ocount = ocount + 1
           
# Define (dictionary) list : candidate and votes
    candidatevote = {"Khan": kcount,"Correy": ccount,"Li" :lcount, "O'Tooley": ocount}
    # Find winner 
    for candidate, value in candidatevote.items():
        if value > max_votecount:
           max_votecount = value
           winner = candidate
# Display results       
print("Election Results")
print("-------------------------------")
print("Total Votes:"+  str(total_votes))
print("-------------------------------")

print(f'Khan: {percentage(kcount,total_votes):.3f}%  ({kcount})')
print(f'Correy: {percentage(ccount,total_votes):.3f}%  ({ccount})')
print(f'Li: {percentage(lcount,total_votes):.3f}%  ({lcount})')
print(f'O\'Tooley: {percentage(ocount,total_votes):.3f}%  ({ocount})')
print(f'--------------------------------'+'\n')
print(f'Winner: {winner} '+'\n')
print(f'--------------------------------'+'\n')

#            Display Result
print("Financial Analysis") 
print("--------------------------------")
print("Total Months " + str(total_months))
print("Total " + "$"+ str(total_Profit_Losses))
print("Average " +"$"+ str(int(average_Profit_Losses)))
print("Greatest Increase in Profits " +str(Max_increase_profits_date) +" $" + str(Max_increase_profits_amount))
print("Greatest Decrease in Profits "+ str(Max_decrease_losses_date) + " $" + str(Max_decrease_losses_amount)) 


# export a text file with the results.
with open('Financial Analysis.txt', 'w')as text:
text.write("Financial Analysis"+ "\n") 
text.write("--------------------------------")
text.write("Total Months " + str(total_months)+ "\n")
text.write("Total " + "$"+ str(total_Profit_Losses)+ "\n")
text.write("Average " +"$"+ str(int(average_Profit_Losses))+ "\n")
text.write("Greatest Increase in Profits " +str(Max_increase_profits_date) +" $" + str(Max_increase_profits_amount)+ "\n")
text.write("Greatest Decrease in Profits "+ str(Max_decrease_losses_date) + " $" + str(Max_decrease_losses_amount)+ "\n") 
