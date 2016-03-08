#!/usr/bin/env python

# Computes the reverse complement of a given nucleotide string
# USAGE: rev_comp.py input_sequence


import sys


def reverse_complement(nucleotides):

	seq_str = str(nucleotides).upper()
	rev_seq_str = seq_str[::-1]

	pyr_seq_str = rev_seq_str.replace('A', 'n')
	pyr_seq_str = pyr_seq_str.replace('T', 'A')
	pyr_seq_str = pyr_seq_str.replace('n', 'T')

	final_seq_str = pyr_seq_str.replace('C', 'n')
	final_seq_str = final_seq_str.replace('G', 'C')
	final_seq_str = final_seq_str.replace('n', 'G')

	return final_seq_str


print(reverse_complement(sys.argv[1]))