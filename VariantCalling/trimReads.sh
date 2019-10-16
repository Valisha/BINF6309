#!/usr/bin/env bash 
nice -n19 java -jar /usr/local/programs/Trimmomatic-0.36/trimmomatic-0.36.jar PE \
-threads 1 -phred33 \
SRR6808334_1.fastq \
SRR6808334_2.fastq \
SRR6808334.R1.paired.fastq \
SRR6808334.R1.unpaired.fastq \
SRR6808334.R2.paired.fastq \
SRR6808334.R2.unpaired.fastq \
HEADCROP:0 \
ILLUMINACLIP:/usr/local/programs/Trimmomatic-0.36/adapters/TruSeq3-PE.fa:2:30:10 \
LEADING:20 TRAILING:20 SLIDINGWINDOW:4:30 MINLEN:36 \
1>new.trim.log 2>new.trim.err

