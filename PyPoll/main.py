import os
import csv

# Path to collect data from the Resources folder
Poll_Data_csv = os.path.join('Resources','election_data.csv')

# Initialize variables
candidate_Reg =[]
No_of_votes = 0
total_votes = 0
Count = []
candidates = []

# with open(budget_data_csv, newline="") as csvfile:
with open(Poll_Data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the Header of the file
    csv_header = next(csvreader)

    for i in csvreader:

        # Counting the total number of votes
        total_votes= total_votes + 1

        # Create a canditate List
        candidate_Reg = (i[2])

        # Counting the no of votes for each cadidate
        if candidate_Reg in candidates:
            can_index = candidates.index(candidate_Reg)
            Count[can_index]= Count[can_index]+1
        else:

            candidates.append(candidate_Reg)
            Count.append(1)
    
    Vote_percentages = []
    max_votes = Count[0]
    max_index = 0

    # Display Result
    print("Election Results") 
    print("--------------------------------")
    print("Total Votes " + str(total_votes))
    print("--------------------------------")

    for icount in range(len(candidates)):
        
            vote_percentage = Count[icount]/total_votes*100
        
            Vote_percentages.append(vote_percentage)
            if Count[icount] > max_votes:
                max_votes = Count[icount]
                print(max_votes)
                max_index = icount
    winner = candidates[max_index]
   
    Vote_percentages = [round(i,2) for i in Vote_percentages]

    for icount in range(len(candidates)):
        print(f"{candidates[icount]}: {Vote_percentages[icount]}% ({Count[icount]})")

    print("--------------------------")
    print(f"Winner:  {winner}")
    print("--------------------------")
    
    #export a text file with the results
with open('Financial Analysis.txt', 'w')as text:
    text.write("Election Results\n")
    text.write("-----------------------------\n")
    text.write(f"Total Votes:  {number_votes}\n")
    text.write("-----------------------------\n")
    for icount in range(len(candidates)):
        text.write(f"{candidates[icount]}: {Vote_percentages[icount]}% ({Count[icount]})\n")
        text.write("-----------------------------\n")
        text.write(f"Winner:  {winner}\n")
        text.write("-----------------------------\n")
    
    # Close the text file
    filewriter.close()