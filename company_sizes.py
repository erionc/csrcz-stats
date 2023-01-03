
'''
Script for computing and showing the company size statistics from CSRCZ dataset 
'''

import csv, json, sys, os

# dataset file path
jsonlfile = "./data/csrcz.txt"

# read file json lines from given file path and return them in a list
def file_lines_to_list(file_path):
    '''read json lines and store them in a list that is returned'''
    with open(file_path, "r", encoding='utf-8') as inf:
        # strips \n at the end of each line
        line_list = [json.loads(line) for line in inf]
    return line_list

# percentage of Micro companies
def get_micro_percent(data):
	n_micro = 0
	for dict in data:
		if dict["Size of Company"] == "Micro":
			n_micro += 1
	return n_micro, round(n_micro/len(data)*100, 2) 
	
# compute percentage of Small companies
def get_small_percent(data):
	n_small = 0
	for dict in data:
		if dict["Size of Company"] == "Small":
			n_small += 1
	return n_small, round(n_small/len(data)*100, 2) 
	
# compute percentage of Medium companies
def get_medium_percent(data):
	n_medium = 0
	for dict in data:
		if dict["Size of Company"] == "Medium":
			n_medium += 1
	return n_medium, round(n_medium/len(data)*100, 2) 
	
# compute percentage of Large companies
def get_large_percent(data):
	n_large = 0
	for dict in data:
		if dict["Size of Company"] == "Large":
			n_large += 1
	return n_large, round(n_large/len(data)*100, 2) 
		
if __name__ == "__main__":

	# load the dataset as list of dictionaries
	dict_lst = file_lines_to_list(jsonlfile)

	# compute percentages
	n_micro, p_micro = get_micro_percent(dict_lst)
	n_small, p_small = get_small_percent(dict_lst)
	n_medium, p_medium = get_medium_percent(dict_lst)
	n_large, p_large = get_large_percent(dict_lst)

	n_unknown = len(dict_lst) - n_micro - n_small - n_medium - n_large
	p_unknown = round(100 - p_micro - p_small - p_medium - p_large, 2)

	# to print in tabular format
	from prettytable import PrettyTable

	# create formated statistics
	t = PrettyTable(["Size", "Number", "Percent"])
	t.add_row(["Unknown", n_unknown, p_unknown])
	t.add_row(["Micro", n_micro, p_micro])
	t.add_row(["Small", n_small, p_small])
	t.add_row(["Medium", n_medium, p_medium])
	t.add_row(["Large", n_large, p_large])

	# print formated table
	print(t)

	# plot bar diagram
	import numpy as np
	from matplotlib import pyplot as plt

	# organize the data to plot
	height = [p_unknown, p_micro, p_small, p_medium, p_large]
	bars = ('Unknown', 'Micro', 'Small', 'Medium', 'Large')

	# Create bars with different colors
	graph = plt.bar(bars, height, color=['black', 'red', 'green', 'blue', 'cyan'])
	# Create names on the x-axis
	i = 0
	for p in graph:
		width = p.get_width()
		height = p.get_height()
		x, y = p.get_xy()
		plt.text(x+width/2, y+height*1.01, str(height)+'%', ha='center')
		i += 1

	# Show graph
	plt.show()
	plt.savefig("./company_size.png")




