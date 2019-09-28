#!/usr/bin/env bash 
# indexAll.sh 
bamFile="sorted_bam/"
leftSuffix=".sorted.bam"
for leftInFile in $bamFile*$leftSuffix
do
	pathRemoved="${leftInFile/$bamFile/}"
	sampleName="${pathRemoved/$leftSuffix/}"
	samtools index $bamFile$sampleName$leftSuffix
done

