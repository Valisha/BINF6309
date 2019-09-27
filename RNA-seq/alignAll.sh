#!/usr/bin/env bash 
# buildAll.sh 
# initialize variable to contain the directory of un-trimmed fastq files 
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
# initialize variable to contain the suffix of left reads 
leftSuffix=".R1.fastq"
rightSuffix=".R2.fastq"
pairedOutPath="paired/"
# Loop through all the left read fastq files in $fastqpath 
for leftInfile in $fastqPath*$leftSuffix
do 
	# Remove the path from the filename and assign to pathRemoved 
	pathRemoved="${leftInFile/$fastqPath/}"
	# Remove the left-read suffix from $pathRemoved and assign to suffixRemoved 
	sampleName="$pathRemoved/$leftSuffix/}"
	nice -n19 gsnap -A sam -D . -d AiptasiaGmapDb 

