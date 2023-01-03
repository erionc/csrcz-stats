
'''
Script for computing and showing CSR initiative statistics from CSRCZ dataset 
'''

import csv, json, sys, os, re
from nltk.tokenize import word_tokenize
# to print in tabular format
from prettytable import PrettyTable

# dataset file path
jsonlfile = "./data/csrcz.txt"

# function for text cleaning
def text_clean(text):
	# remove any html markups
	text = re.sub('<[^>]*>', ' ', text)
	# remove non-word caracters
	text = re.sub('[\W]+', ' ', text)
	text = ' '.join(text.split())	# remove 2+ consequetive whitespaces
	return text

# read file json lines from given file path and return them in a list
def file_lines_to_list(file_path):
    '''read json lines and store them in a list that is returned'''
    with open(file_path, "r", encoding='utf-8') as inf:
        # strips \n at the end of each line
        line_list = [json.loads(line) for line in inf]
    return line_list


if __name__ == "__main__":
	# load the dataset
	dict_lst = file_lines_to_list(jsonlfile)
	
	n_empty, ch_min_ini, tok_min_ini, ch_max_ini, tok_max_ini, ch_tot_ini, tok_tot_ini, ch_avg_ini, tok_avg_ini = 0, 1000000000, 1000000000, 0, 0, 0, 0, 0, 0

	for dict in dict_lst:
		ch_this_ini, tok_this_ini = 0, 0
		ini = dict["Initiatives"] 
		if ini == "": 	# if empty
			n_empty += 1 ; continue
		else:
			ini = text_clean(ini)
			ch_this_ini = len(ini)
			tok_this_ini = len(word_tokenize(ini))
			if ch_this_ini < ch_min_ini:
				ch_min_ini = ch_this_ini
			if ch_this_ini > ch_max_ini:
				ch_max_ini = ch_this_ini
			if tok_this_ini < tok_min_ini:
				tok_min_ini = tok_this_ini
			if tok_this_ini > tok_max_ini:
				tok_max_ini = tok_this_ini
			ch_tot_ini += ch_this_ini ; tok_tot_ini += tok_this_ini
			ch_avg_ini = round(ch_tot_ini / len(dict_lst), 2) 
			tok_avg_ini = round(tok_tot_ini / len(dict_lst), 2) 

	# create formated statistics
	t = PrettyTable(["CSR Initiatives", "Min", "Max", "Avg"])
	t.add_row(["Characters", ch_min_ini, ch_max_ini, ch_avg_ini])
	t.add_row(["Characters", tok_min_ini, tok_max_ini, tok_avg_ini])

	# print formated table
	print(t)
