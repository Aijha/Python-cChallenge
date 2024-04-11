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

#Open CSV

with open(electcsvpath) as csvfile:

    electreader = csv.reader(csvfile, delimiter=',')

#Ignore Header
    next(electreader, None)


#  define function
    
def print_election_results(votes_data):

    #Set variables
    
    total_votes = 369711

    votes_per_candidate = [0,0,0]

    candidate_list = []

    vote_percentages = []

    print_results = []

    for row in votes_data:
    
        candidate_name = row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
        
        candidate_position = candidate_list.index(candidate_name)

        votes_per_candidate[candidate_position] += 1

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
    
    print(print_results)  

# Import and Read electcsvpath CSV
    with open(electcsvpath) as csvfile:
        electreader = csv.reader(csvfile, delimiter = ",")

        next(electreader, None)

        print_results = print_election_results(votes_data)

        for txt in print_results:
            print(txt) 

#  Output to Election results to a text file
output_path = os.path.join("/Users/aijhasymone/Desktop/ClassFolder/Python-cChallenge/PyPoll/election.txt")

output_file = 'election.txt'  # Path to the output text file
        
with open(output_path, 'w') as file:

    # def write_results_to_text_file(results, output_file):
   
    #     # total_votes, candidates percentages, winner 
    #     total_votes, candidates, winner  = results

    # with open(output_file, 'w') as file:
    #     # Write the header
    #     file.write("Election Results\n")
    #     file.write("-------------------------\n")
        
    #     # Write total votes
    #     file.write(f"Total Votes: {total_votes}\n")
    #     file.write("-------------------------\n")
        
    #     # Write candidate % results
    #     for candidate, stats in candidates.items():
    #         file.write(f"{candidate}: {stats['percentage']:.3f}% ({stats['votes']})\n")
        
    #     # Write the winner
    #     file.write("-------------------------\n")
    #     file.write(f"Winner: {winner}\n")
    #     file.write("-------------------------\n")
    
    def main():
#     Specify the input CSV file and output text file
        votes_data = 'electcsvpath'  # Path to the CSV file
        output_file = 'election.txt'  # Path to the output text file
    
    # Analyze votes and get the results
    results = print_election_results(votes_data)
    
    # Write results to the specified output file
    write_results_to_text_file(results, output_file)
    
    # Notify the user that results were written to the file
    print(f"Results written to {output_file}")

# if __name__ == "__main__":
#     main()