#!/usr/bin/env python
'''USAGE: subsample_fasta.py file.fasta --size n --total n' --pair y/n --iters 1
Randomly subsamples a fasta file to the given size, handles both single and paired-end read data
'''

# It's important to know the correct number of sequences per file for this script to run properly,
# please run seq_stats.py prior to running subsample_fasta.py

import sys
import random
import argparse
from itertools import izip


parser = argparse.ArgumentParser(description='Subsample reads from a fasta file.')
parser.add_argument('--reads', default='none', help='Single-end read file')
parser.add_argument('--forward', default='none', help='Forward paired-end read.')
parser.add_argument('--reverse', default='none', help='Reverse paired-end read.')
parser.add_argument('--size', default=0, help='Number of sequences to subsample (# of pairs for paired-end)')
parser.add_argument('--total', default=0, help='Total number of sequences in the fasta file')
parser.add_argument('--paired', default='n', help='Indicates if the file(s) are paired-end reads')
parser.add_argument('--iters', default=1, help='How many times to perform rarefaction')
args = parser.parse_args()

if int(args.size) == 0 or int(args.total) == 0:
	print('ERROR: File or subsample value are of size 0. Quitting.')
	sys.exit()
elif int(args.size) >= int(args.total):
	print('ERROR: Subsample size is smaller than total sequences. Quitting.')
	sys.exit()
elif args.reads == 'none':
	if args.forward == 'none' or args.reverse == 'none':
		print('ERROR: Input file(s) not provided. Quitting.')
		sys.exit()
	
	
# Check if the subsample is that same or larger than the total sequence count, and then
# generates a random list of positions to pick from fasta file
print 'Creating subsampling distribution...'

sample_list = range(1, int(args.total) + 1)
sample_set = sorted(random.sample(sample_list, int(args.size)))
remaining = int(args.iters) - 1

while remaining > 0:
	sample_set = sample_set + sorted(random.sample(sample_list, int(args.size)))
	remaining = remaining - 1
sample_set = set(sample_set)


# Label the input as pe or se
if args.paired == 'y':
	file_type = 'Paired-end'
else:
	file_type = 'Single-end'


# Get output files ready
if args.paired == 'y':
	# Name and open output file
	outfile_str1 = str(args.forward).rstrip('fasta') + 'pick.fasta' 
	outfile1 = open(outfile_str1, 'w')
	outfile_str2 = str(args.reverse).rstrip('fasta') + 'pick.fasta' 
	outfile2 = open(outfile_str2, 'w')

	# Create logfile of subsampling
	logfile_str = str(args.reads).rstrip('fasta') + 'pick.log' 
	logfile = open(logfile_str, 'w')

	log_str = '''Input file names : {infile1} {infile2}
Input file types:  {type}
Output file names: {outfile1} {outfile2}
Total sequences: {total}
Subsample size: {size}
'''.format(infile1=str(args.forward), infile2=str(args.reverse), type=file_type, outfile1=outfile_str1, outfile2=outfile_str2, total=str(args.total), size=str(int(args.size)))
	logfile.write(log_str)
	logfile.close()
else:
	# Name and open output file
	outfile_str = str(args.reads).rstrip('fasta') + 'pick.fasta' 
	outfile = open(outfile_str, 'w')

	# Create logfile of subsampling
	logfile_str = str(args.reads).rstrip('fasta') + 'pick.log' 
	logfile = open(logfile_str, 'w')
	log_str = '''Input file name: {infile}
Input file type:  {type}
Output file name: {outfile}
Total sequences: {total}
Subsample size: {size}
'''.format(infile=str(args.reads), type=file_type, outfile=outfile_str, total=str(args.total), size=str(int(args.size)))
	logfile.write(log_str)
	logfile.close()

# Open and begin looping through fasta file and picking sequences
print 'Writing subsampled fasta file...'

if args.paired == 'y':
	
	seq_count = 0
	include = 0
	iteration = 0
	
	for line_1, line_2 in izip(open(args.forward, 'r'), open(args.reverse, 'r')):
	
		if line_1[0] == '>':
		
			include = 0
			seq_count += 1
			iteration += 1
		
			if iteration == 10000:
				iteration = 0
				progress_str = str(seq_count) + ' of ' + str(args.total)
				print(progress_str)

			if seq_count in sample_set:
				sample_set.discard(seq_count)
				outfile1.write(line_1)
				outfile2.write(line_2)
				include = 1
				continue
	
		elif line_1[0] != '>' and include == 1: 
				outfile1.write(line_1)
				outfile2.write(line_2)
				continue
					
	outfile1.close()
	outfile2.close()
	

else:
	with open(args.reads, 'r') as infile:
		
		seq_count = 0
		include = 0
		iteration = 0
	
		for line in infile:
				
			if line[0] == '>':
			
				include = 0
				seq_count += 1
				iteration += 1
			
				if iteration == 10000:
					iteration = 0
					progress_str = str(seq_count) + ' of ' + str(args.total)
					print(progress_str)

				if seq_count in sample_set:
					sample_set.discard(seq_count)
					outfile.write(line)
					include = 1
					continue
		
			elif line[0] != '>' and include == 1: 
					outfile.write(line)
					continue
						
	outfile.close()			


print 'Done.'
