# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
#CREATE A LIST, DICTIONARY FOR THE COUNTIES
county_options = []
county_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#TRACK THE WINNING COUNTY
winning_county = ""
c_winning_count = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        #GET THE COUNTY NAME FROM EACH ROW
        county_name = row[1]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # IF COUNTY NOT IN COUNTY, ADD THAT COUNTY TO THE LIST
        if county_name not in county_options:
            #ADD THE COUNTY TO THE COUNTY LIST
            county_options.append(county_name)
            #AND BEGIN TRACKING THAT COUNTY VOTE COUNT
            county_votes[county_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        f"County Votes:"
        f"\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
   
    for county in county_votes:
        # Retrieve vote count and percentage.
        c_votes = county_votes[county]
        c_vote_percentage = float(c_votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {c_vote_percentage:.1f}% ({c_votes:,})\n")

        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)

        
        # Determine winning vote count, winning percentage, and winning county.
        if (c_votes > c_winning_count):
            c_winning_count = c_votes
            winning_county = county

    
    # Print the winning county's results to the terminal.
    winning_county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    # Save the winning county's results to the text file.
    txt_file.write(winning_county_summary)
    
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)


        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage


    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
   