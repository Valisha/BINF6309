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
    for kmer in kmer_list:
        if kmer in kmer_dict:
            kmer_dict[kmer] +=1 
        else:
            kmer_dict[kmer]=0
    uni = []
    for kmer in kmer_dict.keys():
        if kmer_dict[kmer]==0:
             uni.append(kmer)
print(len(kmer))
        
   

