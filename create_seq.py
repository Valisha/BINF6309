#!/usr/bin/env python3 
# import seq, seqRecord and seqID 
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord 
from Bio import SeqIO 
sequences = []
# instantiate SeqRecord as my_seq1 and 2. Notice that SeqRecord requires a sequence, so we just instantiate the Seq within the constructor for the SeqRecord 
my_seq1 = SeqRecord(Seq("AGTACACTGGT"), id = "seq1", description = "kmer1")
my_seq2 = SeqRecord(Seq("AGTACACTGGC"), id = "seq2", description = "kmer2")
sequences.append(my_seq1)
sequences.append(my_seq2)
# write the SeqRecords within the last sequences as a fasta file 
SeqIO.write(sequences, "kmers.fasta", "fasta")
print(sequences)
