# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:02:23 2020

@author: tonyz
"""

#HomeWork Budget_Data
#@Author: BCSUWA_Tony_Zhao 18/12/2020

import os
import csv

file_name = "resources/budget_data.csv"
with open(file_name, newline = '', encoding="utf8") as f:

    lines = csv.reader(f, delimiter = ",")

    budget_dict = {}

    for i in lines:
        budget_dict.update ({i[0] : i[1]})
    
budget_dict.pop('Date')
    
general_pl = 0
lastpl = 0
changesum = 0
max_p = 0
max_pd = " "
max_l = 0
max_ld = " "
    
for j in budget_dict.keys():
    general_pl = general_pl + int(budget_dict.get(j))
    if j != "Jan-10": changesum += int(budget_dict.get(j)) - lastpl
    
    #print(int(budget_dict.get(j)))
    #print(changesum)

    if int(budget_dict.get(j)) > max_p:
        max_p = int(budget_dict.get(j))
        max_pd = j

    if int(budget_dict.get(j)) < max_l:
        max_l = int(budget_dict.get(j))
        max_ld = j       
     
    lastpl = int(budget_dict.get(j))
    #print(lastpl)

ave_change = changesum / (len(budget_dict) - 1)

print(ave_change)

dotline = "-" * 50 +"\n"
line = list(range(7))

line[0] = "Finacial Analysis \n"
line[1] = dotline
line[2] = "Total Months: {:2d}, \n".format(len(budget_dict))
line[3] = "Total: ${:10d}, \n".format(general_pl)
line[4] = "Average Change: ${:0.2f}, \n".format(ave_change)
line[5] = "Greatest Increase in Profit: {0}, {1:0.2f}, \n".format(max_pd, max_p)
line[6] = "Greatest decrease in profit: {0}, {1:0.2f}, \n".format(max_ld, max_l)

file_path = os.path.join("analysis", "pybudget_result.txt")
with open(file_path, "w", newline = '') as res:
    
    for i in range(7):
        res.writelines(line[i])
    



