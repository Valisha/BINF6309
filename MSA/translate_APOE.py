#!/usr/bin/env python3
from Bio import SeqIO
import re
from Bio.Seq import Seq
my_list = []
for record in SeqIO.parse("APOE_refseq_transcript.fasta","fasta"):
    if len(record)%3==0:
        my_prot = record.translate()
        print(my_prot)
        my_list.append(my_prot)
SeqIO.write(my_list,"apoe_aa.fasta", "fasta")    
