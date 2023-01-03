
'''
Script for computing and showing the employee statistics from CSRCZ dataset 
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

# employee statistics in Micro companies
def get_micro_percent(data):
	n_micro, emp_micro, min_emp_micro, max_emp_micro = 0, 0, 1000000, 0 
	for dict in data:
		if dict["Size of Company"] == "Micro":
			n_micro += 1
			emp_micro += dict["Number of employees"]
			if dict["Number of employees"] < min_emp_micro:
				min_emp_micro = dict["Number of employees"]
			if dict["Number of employees"] > max_emp_micro:
				max_emp_micro = dict["Number of employees"]
	return n_micro, emp_micro, min_emp_micro, max_emp_micro, round(emp_micro/n_micro, 2) 
	
# employee statistics in Small companies
def get_small_percent(data):
	n_small, emp_small, min_emp_small, max_emp_small = 0, 0, 1000000, 0 
	for dict in data:
		if dict["Size of Company"] == "Small":
			n_small += 1
			emp_small += dict["Number of employees"]
			if dict["Number of employees"] < min_emp_small:
				min_emp_small = dict["Number of employees"]
			if dict["Number of employees"] > max_emp_small:
				max_emp_small = dict["Number of employees"]
	return n_small, emp_small, min_emp_small, max_emp_small, round(emp_small/n_small, 2) 
	
# employee statistics in Medium companies
def get_medium_percent(data):
	n_medium, emp_medium, min_emp_medium, max_emp_medium = 0, 0, 1000000, 0 
	for dict in data:
		if dict["Size of Company"] == "Medium":
			n_medium += 1
			emp_medium += dict["Number of employees"]
			if dict["Number of employees"] < min_emp_medium:
				min_emp_medium = dict["Number of employees"]
			if dict["Number of employees"] > max_emp_medium:
				max_emp_medium = dict["Number of employees"]
	return n_medium, emp_medium, min_emp_medium, max_emp_medium, round(emp_medium/n_medium, 2) 
	
# employee statistics in Large companies
def get_large_percent(data):
	n_large, emp_large, min_emp_large, max_emp_large = 0, 0, 1000000, 0 
	for dict in data:
		if dict["Size of Company"] == "Large":
			n_large += 1
			emp_large += dict["Number of employees"]
			if dict["Number of employees"] < min_emp_large:
				min_emp_large = dict["Number of employees"]
			if dict["Number of employees"] > max_emp_large:
				max_emp_large = dict["Number of employees"]
	return n_large, emp_large, min_emp_large, max_emp_large, round(emp_large/n_large, 2) 

if __name__ == "__main__":

	# load the dataset
	dict_lst = file_lines_to_list(jsonlfile)

	n_micro, emp_micro, min_emp_micro, max_emp_micro, avg_emp_micro = get_micro_percent(dict_lst)
	n_small, emp_small, min_emp_small, max_emp_small, avg_emp_small = get_small_percent(dict_lst)
	n_medium, emp_medium, min_emp_medium, max_emp_medium, avg_emp_medium = get_medium_percent(dict_lst)
	n_large, emp_large, min_emp_large, max_emp_large, avg_emp_large = get_large_percent(dict_lst)

	# to print in tabular format
	from prettytable import PrettyTable

	# create formated statistics
	t = PrettyTable(["Company", "Min", "Max", "Avg"])
	t.add_row(["Micro", min_emp_micro, max_emp_micro, avg_emp_micro])
	t.add_row(["Small", min_emp_small, max_emp_small, avg_emp_small])
	t.add_row(["Medium", min_emp_medium, max_emp_medium, avg_emp_medium])
	t.add_row(["Large", min_emp_large, max_emp_large, avg_emp_large])

	# print formated table
	print(t)

	# plot bar diagram
	import numpy as np
	from matplotlib import pyplot as plt

	# organize the data to plot
	height = [avg_emp_micro, avg_emp_small, avg_emp_medium, avg_emp_large]
	bars = ('Micro', 'Small', 'Medium', 'Large')

	# Create bars with different colors
	graph = plt.bar(bars, height, color=['red', 'green', 'blue', 'cyan'])
	# Create names on the x-axis
	i = 0
	for p in graph:
		width = p.get_width()
		height = p.get_height()
		x, y = p.get_xy()
		plt.text(x+width/2, y+height*1.01, str(height), ha='center')
		i += 1

	# Show graph
	plt.show()
	plt.savefig("./employee_distribution.png")




