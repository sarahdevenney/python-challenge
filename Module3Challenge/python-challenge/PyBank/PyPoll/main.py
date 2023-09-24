import csv

#open file, use DictReader so it skips the header
with open(r".\Resources\election_data.csv", 'r') as file_handle:
    row_list = list(csv.DictReader(file_handle))

#count the number of rows in the votes list to determine total votes
total_votes = len(row_list)

#create a text file to print results to
out_file_h = open(r'analysis\voting_analysis.txt','w')

#print header and total votes to terminal and text file
print("Election results\n-------------------------")
print("Election results\n-------------------------", file=out_file_h)
print("Total Votes:", total_votes)
print("Total Votes:", total_votes, file=out_file_h)
print("-------------------------")
print("-------------------------", file=out_file_h)

#create a dictionary of the canditates with their assigned value being their total number of votes
#loop through these dictionaries to find who had the highest number of votes
can_vote_dict = {}
for row in row_list:
    if row['Candidate'] in can_vote_dict:
        can_vote_dict[row['Candidate']] += 1
    else:
        can_vote_dict[row['Candidate']] = 1

#create a tuple to default as nobody to compare each candidate against
winner = ("nobody", -1)
#if candidate has more votes than previous candidate they replace as winner otherwise it stays as previous winner
for can, votes in can_vote_dict.items():
    print(f'{can}: {votes/total_votes:.3%} ({votes})')
    print(f'{can}: {votes/total_votes:.3%} ({votes})', file=out_file_h)
    if votes > winner[1]:
        winner = (can, votes)
#print results
print("-------------------------")
print("-------------------------", file=out_file_h)
print(f'winner: {winner[0]}')
print(f'winner: {winner[0]}', file=out_file_h)
print("-------------------------")
print("-------------------------", file=out_file_h)
#close text file 
out_file_h.close()