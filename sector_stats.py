
'''
Script for computing and showing industry sector statistics from CSRCZ dataset 
'''

import csv, json, sys, os, re
from nltk.tokenize import word_tokenize
# to print in tabular format
from prettytable import PrettyTable

# dataset file path
jsonlfile = "./data/csrcz.txt"

# read file json lines from given file path and return them in a list
def file_lines_to_list(file_path):
    '''read json lines and store them in a list that is returned'''
    with open(file_path, "r", encoding='utf-8') as inf:
        # strips \n at the end of each line
        line_list = [json.loads(line) for line in inf]
    return line_list
	
# find and return frequency of each sector 
def sector_frequency(sector_lst):
	dic = {}
	for word in sector_lst:
		if word in dic:
			dic[word] += 1
		else:
			dic[word] = 1
	return dic
	
if __name__ == "__main__":
	# load the dataset
	dict_lst = file_lines_to_list(jsonlfile)
	sect_lst = []
	
	# get all sectors in a list
	for d in dict_lst:
		this_sector = d["Sector"]
		sect_lst.append(this_sector)
	
	# get frequency for each sector
	freq = sector_frequency(sect_lst)

	# create formated statistics
	t = PrettyTable(["Sector", "Number", "Percent"])

	# print frequency in number and percent 
	for k,v in freq.items():
		percent = round(v / len(dict_lst) * 100, 2)
		# rename the "" sector to "Unknown"
		if k == "":
			t.add_row(["Unknown", v, percent])
		else:
			t.add_row([k, v, percent])
		
	# print formated table
	print(t)
