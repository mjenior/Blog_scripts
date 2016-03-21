#!/usr/bin/env python 

#  USAGE:  rarefy.py input_file subsample
# Rarefies a single column file of numbers to a given level and then outputs it to a new file

import sys
import random


with open(sys.argv[1], 'r') as infile:
	
	collection = []
	current = 0
	sample = int(sys.argv[2])
	
	for line in infile:
		current += 1
		group = int(line)
		rep_group = [current] * group
		collection = collection + rep_group
		
	random.shuffle(collection)
	selection = collection[:sample]
	selection = sorted(selection)
	

out_str = str(sys.argv[1]).strip('txt') + 'pick.txt'
with open(out_str, 'w') as outfile:

	for index in range(0, current):
		entry = str(selection.count(index)) + '\n'
		outfile.write(entry)