#!/usr/bin/env python

# Annotates Fasta file with best BLAST results (tab-delimitted)
# USAGE: parse_blast.py blast_results query_fasta_file annotated_fasta_file_name


import sys


# Read the best hits from the BLAST output into a python dictionary
with open(sys.argv[1], 'r') as blast_file:

	result_dict = {}
	unique_genes = set()

	for line in blast_file:

		queryId, subjectId, percIdentity, alnLength, mismatchCount, gapOpenCount, queryStart, queryEnd, subjectStart, subjectEnd, eVal, bitScore = line.split('\t')
		
		percIdentity = float(percIdentity)
		
		base = int(str(eVal).split('e-')[0])
		exponent = (10 ^ int(str(eVal).split('e-')[1]))
		eVal = float(base / exponent)
		
		bitScore = float(bitScore)
		
		if percIdentity < 50.0 and eVal > 0.00005 and bitScore > 50.0: continue
		
		entry = [subjectId, percIdentity, bitScore, eVal]
		
		if not queryId in unique_genes:
			result_dict[queryId] = '\t'.join(entry)
			unique_genes.update(queryId)
		else:
			prev_entry = result_dict[queryId]
			if prev_entry[1] < entry[1] or prev_entry[2] > entry[2] or prev_entry[3] < entry[3]:
				result_dict[queryId] = '\t'.join(entry)
				

# Annotate the query fasta file with the best BLAST hits
with open(sys.argv[2], 'r') as fasta_file:

	new_fasta = open(sys.argv[3], 'w')
	

	while True:
	
    	entry_line = fasta_file.readline()
    	entry_line = entry_line.strip()
    	entry_line = entry_line.lstrip('>')
    	
    	seq_line = fasta_file.readline()
    	
    	try:
    		annotation = str(result_dict[entry_line]) + '\n'
    	except KeyError:
    		continue
    	
    	new_fasta.write(annotation)
    	new_fasta.write(seq_line)
    	
    	if not entry_line:
    		break
    	elif not entry_line:
    		break
    
    
    new_fasta.close()
    
    
    
    