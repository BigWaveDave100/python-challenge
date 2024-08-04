# Dependencies
import csv
# Set variables
net_votes = 0
candidate_votes = {}
# Set path and skip header row
with open("PyPoll/Resources/election_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
# Loop through csv file and add up votes
    for row in csvreader:
        candidate = row[2]
        net_votes += 1
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
# determine highest number of votes and declare the winner
victor = max(candidate_votes, key=candidate_votes.get)
# display results
results = []
results.append(f"Election Results")
results.append(f"----------------------")
results.append(f"Total Votes: {net_votes}")
results.append("----------------------")
for candidate in candidate_votes:
    vote_count = candidate_votes[candidate]
    vote_percentage = (vote_count / net_votes) * 100
    results.append(f"  {candidate}: {vote_percentage:.3f}% ({vote_count})")
results.append(f"----------------------")
results.append(f"Winner: {victor}")
# display in terminal
for line in results:
    print(line)
# display in text file
with open('election_analysis.txt', 'w') as txtfile:
    for line in results:
        txtfile.write(line + '\n')