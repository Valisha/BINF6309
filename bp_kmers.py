#!/usr/bin/env python3 
# reading the drosaphila fasta file 
from Bio import SeqIO
import re
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
def occurs_once(a,item):
    return a.count(item)==1
for record in SeqIO.parse("/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta","fasta"):
    sequence = str(record.seq)
    #print(sequence)
    #mysequence = Seq(sequence, generic_dna)
    kmer_list = []
    for i in range(len(sequence)):
        seq = sequence[i:i+6]
        if (len(seq)) == 6: 
            kmer_list.append(str(seq))
    kmer_dict = {}
    for i in range(len(kmer_list)):
        kmer_dict.update({kmer_list[i]:kmer_list.count(kmer_list[i])})
    print(kmer_dict)

