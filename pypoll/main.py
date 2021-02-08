import csv
from math import * #from zybooks
with open('pypoll.csv') as r:
    string = csv.reader(r,delimiter=',')
    next(string)
    totalvoters = 0 #  voter count
    candidates = {} #  dictionary for the candidates
    for row in string:
        totalvoters += 1 # add a voter to total count all rows
        if row[2] in candidates: 
            candidates[row[2]] += 1 # adds a vote 
        else: # or else
            candidates[row[2]] = 1 # adds to dict
    candidatelist = [candidates.keys()] # list of names
    candidatevotes = [candidates.values()] #list o values
    maxvotes = max(candidatevotes) 
    winner = candidatelist[candidatevotes.index(maxvotes)]
    print("Election Results:")
    print("_____________________________")
    print("Total Votes: {}".format(totalvoters))
    print("_____________________________")
    for candidate in candidates:
        print("{}: {}% ({})".format(candidate,round(candidates[candidate]/totalvoters*100,2),candidates[candidate]))
    print("______________________________")
    print("Winner: {}".format(winner))
    print("______________________________")
