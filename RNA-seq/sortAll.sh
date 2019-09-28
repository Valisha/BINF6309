#!/usr/bin/env bash 
#sortAll.sh 
leftSuffix=".sam"
samPath="sam_folder/"
rightSuffix=".sorted.bam"
for leftInFile in $samPath*$leftSuffix
do 
	pathRemoved="${leftInFile/$samPath/}"
	sampleName="${pathRemoved/$leftSuffix/}"
	echo $samPath$sampleName$leftSuffix
	samtools sort $samPath$sampleName$leftSuffix -o $sampleName.sorted.bam 1>$sampleName.sort.log 2>$sampleName.sort.err
done 
#samtools sort Aip02.sam -o Aip02.sorted.bam 1>Aip02.sort.log 2>Aip02.sort.err 
