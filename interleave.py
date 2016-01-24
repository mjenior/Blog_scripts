#!/usr/bin/env python
'''USAGE: interleave.py read1.fasta read2.fasta paired.fasta
Interleaves two paired-end fasta read files
'''
import sys
from itertools import izip

with open(sys.argv[3], 'w') as outfile:

	entries = 0
	
	for line_1, line_2 in izip(open(sys.argv[1], 'r'), open(sys.argv[2], 'r')):

		if line_1 == '\n' and line_2 == '\n': continue
					
		elif line_1[0] == '>' and line_2[0] == '>':
			entry1 = line_1
			entry2 = line_2
			entries = 1
			continue
			
		elif entries == 1:
			seq1 = line_1
			seq2 = line_2
			entries = 0
			
		outfile.write(entry1)
		outfile.write(seq1)
		outfile.write(entry2)
		outfile.write(seq2)