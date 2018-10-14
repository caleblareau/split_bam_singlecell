#!/usr/bin/env python

import sys
import re
import os
import pysam
from optparse import OptionParser
from contextlib import contextmanager

# Parse out data
opts = OptionParser()
usage = "usage: %prog [options] [inputs] Software to process aligned bam files and split based on some attribute"
opts = OptionParser(usage=usage)
opts.add_option("-i", "--input", help="Filename of new .bam file to be generated")
opts.add_option("-d", "--dict-file", help="Filepath of the dictionary to split attribut by")
opts.add_option("-t", "--sam-tag", help="two letter sam tag needed for file splitting")

options, arguments = opts.parse_args()

inbam = options.input
dictfile = options.dict_file
tagofinterest = options.sam_tag

print("looking for tag: " + tagofinterest)


bam = pysam.AlignmentFile(inbam, "rb")
basename = re.sub(".bam$", "", os.path.basename(inbam))

def getTag(intags, tag):
    '''
    Checks for specific tag from CLI
	'''
    for tg in intags:
    	if(tag == tg[0]):
    		return(tg[1])
    return("NA")

# Parse a dictionary file
d = {}
with open(dictfile) as f:
  for line in f:
    tok = line.split()
    d[tok[0]] = tok[1].strip()
    
unique_values = list(set(d.values()))
unique_keys = set(d.keys())

# Function to open lots of files
@contextmanager
def multi_file_manager(files, mode='rt'):
    """ Open multiple files and make sure they all get closed. """
    #print(files)
    files = [pysam.AlignmentFile(file, "wb", template = bam) for file in files]
    yield files
    for file in files:
        file.close()

files = [basename + "." + bc + ".bam" for bc in unique_values]

# Open all the output files and spit out the filtered data
# Based on where the matching value originates
with multi_file_manager(files) as fopen:
	for read in bam.fetch():
		tag = getTag(read.tags, tagofinterest)
		if(tag in unique_keys):
			dict_tag = d[tag]
			idx = unique_values.index(dict_tag)
			fopen[idx].write(read)