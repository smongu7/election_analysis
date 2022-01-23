#!C:/Users/smong/anaconda3/python.exe 
# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add dependencies.
import csv 
import os

# Add a variable to load a file to a path
file_to_load = os.path.join('c:/Users/smong/Documents/Classwork/module_3/election_analysis/resources_3', 'election_results.csv')

# Add a variable to save the file to a path.
file_to_save = os.path.join("c:/Users/smong/Documents/Classwork/module_3/election_analysis/resources_3", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize a county and candidate list and dictionary
# 1a. Candidates
candidates = []
candidate_votes = {}
# 1b. Counties
county = []
county_votes = {}

# Initialize an empty string, and a variable 
# for the winning candidate and county, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""
county_vote = 0
winning_county_count = 0

# Open election results and read file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)

    # Print each row in CSV
    for row in file_reader:
        # Add to total vote count
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidates:
            # Add it to the list of candidates.
            candidates.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1


        # If county does not match existing county
        if county_name not in county:
            #Add to list of counties
                county.append(county_name)

            # Begin tracking that county's votes
                county_votes[county_name] = 0

        # Add a vote to that county's count
        county_votes[county_name] += 1

    # Save results to text file
    with open(file_to_save, "w") as txt_file:
 
    # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
            f"\nCounty Votes:\n")
        print(election_results, end="")    
        # Save the final vote count to the text file.
        txt_file.write(election_results)
    
        # Iterate through county list           
        for county_name in county_votes:
            # Retrieve vote count of a county
            votes_county = county_votes[county_name]
            # Calculate the percentage of votes for each county.
            county_percentage = float(votes_county) / float(total_votes) * 100
            # Print each county's name, vote count and percentage to terminal
            county_results = (f"{county_name}: {county_percentage:.1f}% ({votes_county:,})\n")
            print(county_results)
            # Save the county results to our text file.
            txt_file.write(county_results)

            #Determine county with largest turnout
            if (votes_county > winning_county_count):
                winning_county = county_name
                winning_county_count = votes_county

                winning_county_summary = (
                    f"-------------------------\n"
                    f"Largest County Turnout: {winning_county}\n"
                    f"-------------------------\n")
        print(winning_county_summary)
        txt_file.write(winning_county_summary)
    
        # Determine percentage of votes for each candidate
        # Iterate through candidate list
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            # Print each candidate's name, vote count and percentage to terminal
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
            
                winning_candidate_summary = (
                        f"-------------------------\n"
                        f"Winner: {winning_candidate}\n"
                        f"Winning Vote Count: {winning_count:,}\n"
                        f"Winning Percentage: {winning_percentage:.1f}%\n"
                        f"-------------------------\n")

        print(winning_candidate_summary) 
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary) 