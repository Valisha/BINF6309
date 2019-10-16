author: “Valisha Shah (Valisha)” title: “Variant Calling” output:
md\_document: variant: gfm \_\_\_

Methods
=======

-   getGenome.sh getGenome uses “wget” command to retrieve reference
    genome from an online database
-   getReads.sh getReads uses fastq-dump to get the NGS reads used in
    the comparison paper
-   trimReads.sh trimReads uses trimmomatic a java program to trim the
    leading, trailing and also returns the paried and unpaired sequences
    from the reads that are downloaded
-   indexGenome.sh indexGenome uses bwa (burrows-wheeler algorithm) to
    index the genome
-   alignReads.sh alignReads aligns the reads using bwa-mem again from
    the bwa program to get the aligned reads from the reference genome
    and the fastq files
-   analyzeVariants.sh producing a VCF file using DeepVariant
