#1. total number of votes cast
#2. list of candidates with more than 0 votes
#3. % of each votes given to each cand
#4. total number of votes each cand got
#5. winner of election based on popvote


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Assign a total votes variable
total_votes = 0
#Assign a candidate list variable
candidate_options = []
#assign a votes per candidate dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here. 
    file_reader = csv.reader(election_data)
    
    # Skip the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #increment total votes
        total_votes = total_votes + 1
        #set value for name of cand
        candidate_name = row[2]
        #add cand name to array if unique
        if candidate_name not in candidate_options:
            #add cand name to array if uniuqe
            candidate_options.append(candidate_name)
            #start tracking votes for that cand
            candidate_votes[candidate_name] = 0
        
        #start tallying votes for each candidate
        candidate_votes[candidate_name] += 1 
    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        share = int(votes)/int(total_votes)*100
        print(f"{candidate}: {share:.1f}% ({votes:,})\n")
    
        if (votes > winning_count) and (share > winning_percentage):
             # If true then set winning_count = votes and winning_percent =
             # vote_percentage.
             winning_count = votes
             winning_percentage = share
             # And, set the winning_candidate equal to the candidate's name.
             winning_candidate = candidate

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
