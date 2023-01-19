import os
import csv


#import csv file 

election_data = os.path.join("/Users/Crisaldry/Documents/GitHub/python-challenge/Instructions 8/PyPoll/Resources/election_data.csv")

#PyPoll Variables
ballot_ID = []
county = []
candidates = []
candidates_list =[] #candidate options 
candidates_voted = {} #dictionary 
#total_num_votes_cast = []
#list_candidates_voted = []
#number_votes_candidates = 0
#percent_votes_won = []
popular_votes_winner = []
popular_vote_candidate = []
candidate_names = []

#open election_data.csv file

with open(election_data, encoding="UTF") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skip the header

    for row in csvreader:
        ballot_ID.append(row[0])
        county.append(row[1])
        # candidates.append(row[2])

    #total number of votes cast 
        total_num_votes_cast = str(len(ballot_ID))

    #complete list of candidates who received votes
        # function to find number of votes in an election where votes
        # are represented as candidate names
    # for row in csvreader:
        candidates =row[2]
        if candidates not in candidates_list:
            candidates_list.append(candidates)
            candidates_voted[candidates]=0
        candidates_voted[candidates] += 1
        votes = candidates_voted.get(candidates)
        vote_percentage = str(float(votes) / float(total_num_votes_cast) *100)
        #vote percentages
        


    # winner based on popular votes
    popular_votes_winner = max(votes) #giving the max by alphabetical name not by votes. 


# Result print statements 
print("\n"+"Election Results"+"\n")
print("------------------------------"+"\n")
print("Total Votes: "+total_num_votes_cast+"\n")
print("------------------------------"+"\n")
print(str(candidates_voted))
print(popular_votes_winner)
#Result text file
with open("/Users/Crisaldry/Documents/GitHub/python-challenge/Instructions 8/PyPoll/Resources/PyPoll_Results.txt", mode="w") as resultfile:
    resultfile.write("\n"+"Election Results"+"\n")
    resultfile.write("------------------------------"+"\n")
    resultfile.write("Total Votes: "+total_num_votes_cast+"\n")
    resultfile.write("------------------------------"+"\n")
    resultfile.write(str(candidates_voted))


