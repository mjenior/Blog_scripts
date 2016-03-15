#!/usr/bin/env python

# USAGE:  fasta_diffs.py fasta_1 fasta_2 output_1 output_2

import sys


with open(sys.argv[1], 'r') as infile_1:
	
	file_1 = set()
	file_1_dict = {}
	reading = 0
	
	for line in infile_1:
		
		if line == '\n': continue
		
		elif line.startswith('>'):
			reading = 1
			
			entry = line.rstrip('\n')
			entry = entry.lstrip('>')
			file_1 = file_1 | {entry}
			
		elif reading == 1:
			reading = 0
			file_1_dict[entry] =  line
	
	print('File 1 gene count: ' + str(len(file_1)))
					

with open(sys.argv[2], 'r') as infile_2:

	file_2 = set()
	file_2_dict = {}
	reading = 0
	
	for line in infile_2:
		reading = 1
		
		if line == '\n': continue
		
		elif line.startswith('>'):
			
			entry = line.rstrip('\n')
			entry = entry.lstrip('>')
			file_2 = file_2 | {entry}
			
		elif reading == 1:
			reading = 0
			file_2_dict[entry] =  line

	print('File 2 gene count: ' + str(len(file_2)))
	

file_1_only = file_1.difference(file_2)
print('File 1 only genes: ' + str(len(file_1_only)))

file_2_only = file_2.difference(file_1)
print('File 2 only genes: ' + str(len(file_2_only)))


all_diffs = file_1_only.union(file_2_only)
print('Total differences found: ' + str(len(all_diffs)))
	
	
with open(sys.argv[3], 'w') as outfile_1:
	for index in list(file_1_only):
		seq = file_1_dict[index]
		entry = '>' + index + '\n'
		outfile_1.write(entry)
		outfile_1.write(seq)
		outfile_1.write('\n')
	
with open(sys.argv[4], 'w') as outfile_2:
	for index in list(file_2_only):
		seq = file_2_dict[index]
		entry = '>' + index + '\n'
		outfile_2.write(entry)
		outfile_2.write(seq)
		outfile_2.write('\n')	
	
	
	
