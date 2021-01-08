# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:45:09 2020

@author: tonyz
"""

#Homework PyPoll by BCSUWA_Tony_Zhao 18/12/2020

import os
import csv

filepath = os.path.join("resources", "election_data.csv")
with open(filepath, "r", newline = '', encoding="utf8") as f:

    lines = csv.reader(f, delimiter = ",")

    election_dict = {}
    county_dict = {}

    g_votes = -1

    for i in lines:

        g_votes += 1
    
        if i[2] in election_dict:
            election_dict[i[2]] += 1
        else:
             election_dict.update ({i[2] : 1})
        
        if i[1] in county_dict:
            county_dict[i[1]] += 1
        else:
            county_dict.update ({i[1] : 1})
        
election_dict.pop("Candidate")
county_dict.pop("County")
        
print(g_votes, "\n")
print(election_dict, end= " ")
print("\n")
print(county_dict, end="  ")  

k_perc = int(election_dict["Khan"])/ g_votes 
c_perc = int(election_dict["Correy"]) /g_votes
l_perc = int(election_dict["Li"]) /g_votes
o_perc = int(election_dict["O'Tooley"]) /g_votes

print("\n")

print(k_perc, c_perc, l_perc, o_perc, end = " ")

line = list(range(11))

dotline = "-" * 30 + "\n"

line[0] = "Election Results, \n"  
line[1] = dotline
line[2] = "Total votes: {:10d}, \n".format(g_votes)
line[3] = dotline
line[4] = "Khan : {:0.2%}, {:10d}, \n".format(k_perc, int(election_dict["Khan"]))
line[5] = "Correy : {:0.2%}, {:10d},\n".format(c_perc, int(election_dict["Correy"]))
line[6] = "Li : {:0.2%}, {:10d}, \n".format(l_perc, int(election_dict["Li"]) )
line[7] = "O'Tooley : {:0.2%}, {:10d}, \n".format(o_perc, int(election_dict["O'Tooley"]) )
line[8] = dotline
line[9] = "The Winner: Khan \n"
line[10] = dotline

filetowrite = os.path.join("analysis", "pypoll_result.txt")
with open(filetowrite, "w") as res:
    
    for j in range(11):
        res.writelines(line[j])


