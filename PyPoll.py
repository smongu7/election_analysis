# The data we need to retrieve
# 1. the total number of votes cast
# 2. a complete list of candidates
# 3. percentage of votes each candidate won
# 4. total number of votes each candidate won
# 5. winner of election

# Add our dependencies.
import csv  
import os

#Add a variable to load a file to a path
file_to_load = os.path.join('c:/Users/smong/Documents/Classwork/module_3/election_analysis/resources_3', 'election_results.csv')

# Add a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidates = []
# Declare empty dictionary
candidate_votes = {}
# County List
# county = []
# County dictionary
# county_votes = {}

# Track winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)

    # Print each row in CSV
    for row in file_reader:
        # 2. Add to total vote count
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidates:
            # Add it to the list of candidates.
            candidates.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Determine percentage of votes for each candidate
    # Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: received {vote_percentage}% of the vote.")
        # Print each candidate's name, vote count and percentage to terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    
            winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")

print(winning_candidate_summary)