#Main Script

# The total number of votes cast
# Complete list of candidates who received votes

# Percentage of votes each candidate won
# Total number of votes each candidate won

# Winner of the election based on popular vote


# Import Dependencies
import os
import csv

electcsvpath = os.path.join("/Users/aijhasymone/Desktop/ClassFolder/Python-cChallenge/PyPoll/Resources/election_data.csv")

#Open and Read CSV

with open(electcsvpath) as csvfile:

    electreader = csv.reader(csvfile, delimiter=',')

    next(electreader, None)


# def print_election_results(election_results):
    
def electreader(votes_data):
    for row in votes_data:
        total_votes = 0
        candidates = [dict(int)]

    with open(votes_data, 'r') as file:
        electreader = csv.reader(file)
        
        # Skip header
        next(electreader)
        
        # Iterate through each row in the CSV file
        for row in electreader:
            total_votes += 1
            candidate_name = row[2]
            
            # Count votes for each candidate
            candidates[candidate_name] += 1
    

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        candidates[candidate] = {'votes': votes, 'percentage': percentage}

    winner = max(candidates, key=lambda x: candidates[x]['votes'])

    return total_votes, dict(candidates), winner

def main():
    votes_file = "/Users/aijhasymone/Desktop/ClassFolder/Python-cChallenge/PyPoll/Resources/election_data.csv"  # Change this to the name of your CSV file
    
    total_votes, candidates, winner = analyze_votes(votes_file)
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    for candidate, stats in candidates.items():
        print(f"{candidate}: {stats['percentage']:.3f}% ({stats['votes']})")
    
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

#Set variables
    
    total_votes = 0

    votes_per_candidate = [0,0,0]

    candidate_list = []

    vote_percentages = []

    print_results = []


# Complete list of candidates who received votes
    for row in electreader:

        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)

        candidate_position = candidate_list.index(candidate_name)

        votes_per_candidate[candidate_position] += 1

# The total number of votes cast
        total_votes += 1

# Percentage of votes each candidate won
    for votes in votes_per_candidate:

        percent_per_candidate = round(((votes / total_votes) *100), 3)
        vote_percentages.append(percent_per_candidate)

# Total number of votes each candidate won

        winner_position = vote_percentages.index(max(vote_percentages))
        winner = candidate_list[winner_position]

# Winner of the election based on popular vote
        print_results.append("Election results")

        print_results.append("---------------")

        print_results.append("Total Votes: " + str(total_votes))

        print_results.append("---------------")

    for i, candidate in enumerate(candidate_list):

        print_results.append(candidate + ": " + " %"  + str(vote_percentages[i]) + " (" +  str(votes_per_candidate[i]) + ") ")
    
        print_results.append("--------------")
    
        print_results.append("Winner: "  + winner)

        print_results.append("--------------")

        return print_results  

# Read into electcsvpath
    with open(electcsvpath) as csvfile:
        electreader = csv.reader(csvfile, delimiter = ",")

        next(electreader, None)

        print_results = print_election_results(electreader)

        for txt in print_results:
            print(txt) 

#  Output to TXT File

output_path = os.path.join("/Users/aijhasymone/Desktop/ClassFolder/Python-cChallenge/PyPoll/print_results.txt")

with open(output_path, 'w') as file:

    # for txt in electreader:
        file.write(f"{txt}\n")