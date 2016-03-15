#!/bin/python

# This script eliminates spaces in sequence names and put all residue information on a single line per entry
# USAGE: format_fasta.py input_file output_file

import sys

infile = open(sys.argv[1], 'r')

temp_seq = ''
current = 0

with open(sys.argv[2], 'w') as outfile:
	for line in infile:

		if line == '\n': continue
	
		line = line.strip()
		
		if line[0] == '>':
			if current != 0: outfile.write(temp_seq + '\n')
			seq_name = '|'.join(line.split('  '))
			seq_name = seq_name.replace(' ', '_')
			outfile.write(seq_name + '\n')
			temp_seq = ''
			current += 1
			continue
			
		else:
			temp_seq = temp_seq + line.upper()
		
	outfile.write(temp_seq)

infile.close()
