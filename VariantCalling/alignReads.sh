#!/usr/bin/env bash 
bwa mem -M -t 8 GRCh38.primary_assembly.genome.fa.gz SRR6808334_1.fastq SRR6808334_2.fastq 1>align1.sam 2>align2.sam
