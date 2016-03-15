#!/usr/bin/python
'''USAGE: annotate_fasta.py Fasta BLASToutput annotatedFasta
This script annotates a fasta file with sequence names determined from a BLAST of that file.
'''
import sys

fasta_file = open(sys.argv[1],'r')
output_file = open(sys.argv[3],'w')

# Write dictionary from BLAST output
with open(sys.argv[2],'r') as blast_output:
	blast_dictionary = {}
	for line in blast_output:
		line = line.split()
		query = line[0]
		target = line[1]
		evalue = line[10]
		entry = target + ':evalue_' + str(evalue)
		blast_dictionary[query] = entry

key_errors = 0
start = 0
hypothetical = 0

# Parse the fasta file and print translated names and unchanged sequence data
for line in fasta_file:

	if str(line).startswith('>'):
		start += 1
		
		entry = str(line).strip('>')
		entry = entry.rstrip('\n')
		
		try:
			blast_hit = blast_dictionary[entry]
			if 'hypothetical' in blast_hit: hypothetical += 1
		except KeyError:
			key_errors += 1
			blast_hit = entry + ':Unknown_' + str(key_errors)
		
		final_entry = '>' + blast_hit + '\n'
		output_file.write(final_entry)

	else:
		output_file.write(line)
		if start > 0: output_file.write('\n')

fasta_file.close()
output_file.close()

annotated = start - key_errors
print(str(start)) + ' total sequences.'
print(str(annotated) + ' sequences successfully annotated.')
print(str(hypothetical) + ' sequences annotated as hypothetical.')
print(str(key_errors) + ' sequences could not be annotated.')

