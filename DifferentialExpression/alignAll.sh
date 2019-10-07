#!/usr/bin/env bash 
# alignAll.sh 
outDir="quant/"
fastqPath="/scratch/SampleDataFiles/Paired/"
leftSuffix=".R1.paired.fastq"
rightSuffix=".R2.paired.fastq"
for leftInFile in $fastqPath*$leftSuffix
do
    #Remove the path from the filename and assign to pathRemoved
    pathRemoved="${leftInFile/$fastqPath/}"
    #Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
    sampleName="${pathRemoved/$leftSuffix/}"
    #echo $fastqPath$sampleName$leftSuffix
    #echo $fastqPath$sampleName$rightSuffix
    function align {
    salmon quant -l IU is \
        -1 $fastqPath$samleName$leftSuffix \
        -2 $fastqPath$sampleName$rightSuffix \
        -i AipIndex \
        --validateMappings \
        -o $outDir$sampleName
    }
align 1>align.log 2>align.err
done

