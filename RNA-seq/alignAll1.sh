#!/usr/bin/env bash 
# buildAll.sh 
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
#Initialize variable to contain the suffix for the left reads
leftSuffix=".R1.fastq"
rightSuffix=".R2.fastq"
pairedOutPath="Paired/"
#Loop through all the left-read fastq files in $fastqPath
for leftInFile in $fastqPath*$leftSuffix
do
    #Remove the path from the filename and assign to pathRemoved
    pathRemoved="${leftInFile/$fastqPath/}"
    #Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
    sampleName="${pathRemoved/$leftSuffix/}"
    #Print $sampleName to see what it contains after removing the path
    echo $sampleName
    nice -n19 gsnap -A sam -D . -d AiptasiaGmapDb $pairedOutPath$sampleName$leftSuffix $pairedOutPath$sampleName$rightSuffix 1>$sampleName.sam 2>$sampleName.err

done		#nice -n19 gsnap -A sam -D . -d AiptasiaGmapDb $pairedOutPath$sampleName$leftSuffix $pairedOutPath$sampleName$rightSuffix 1>$sampleName.sam 2>$sampleName.err
#done
