#!/usr/bin/env python3 
from Bio import SeqIO
import itertools 
file1= "/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq"
file2 ="/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq"
file_out = "interleaved.fastq"
formats = "fastq"
def interleave(iter1,iter2):
	for (forward, reverse) in itertools.zip_longest(iter1,iter2):
		assert forward.id == reverse.id
		forward.id += "/1"
		reverse.id += "/2"
		yield forward
		yield reverse 
records_f = SeqIO.parse(open(file1,"rU"),formats)
records_r = SeqIO.parse(open(file2, "rU"), formats)
handle = open(file_out, "w")
count = SeqIO.write(interleave(records_f, records_r), handle, formats) 
handle.close()
print("% i records written as %s"% (count, file_out))
