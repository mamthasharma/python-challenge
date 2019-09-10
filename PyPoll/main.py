#import modules

import os
import csv
from collections import Counter

#Create array to hold values
candidate_list= []
countvotes=Counter()
winner=[]
pc_vote=[]
print_result=[]

#path to the csv file

csvpath = os.path.join('election_data.csv')

#path to the output file
output_path = os.path.join("new.csv")
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    next(csvreader, None) 
    countvote = 0

    for row in csvreader:
        candidate_list.append(row[2])
    
    total_votes = len(candidate_list)
    
    for name in candidate_list:
        countvotes[name] += 1
    # winner = min(zip(countvotes.keys()))

    # print(winner)
    

    candidate = tuple(countvotes.keys())
    candidatevote = tuple(countvotes.values())

    for value in candidatevote:
        pc_vote.append((int(value)/total_votes)*100)

    #print results to the result array    
    print_result.append("Election Results")
    print_result.append("---------------------------------------")
    print_result.append("Total Votes Cast : " + str(total_votes))
    
    for i in range(len(candidate)):
        print_result.append(candidate[i] +"  " + "Percentage " + str(round(pc_vote[i],1))+"% "+ str(candidatevote[i]))
    print_result.append('-----------------------')

    print_result.append(f'Winner: {candidate[0]}')

    print_result.append('-----------------------')
 
    print("\n".join((print_result)))
    
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    for item in print_result:
        csvfile.write('%s\n' % item)
