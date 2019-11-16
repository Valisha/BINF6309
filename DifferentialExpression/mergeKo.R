#!/usr/bin/env Rscript 
# mergeKo.R
# load the kable library to display formatted tables 
library(knitr)
# load the blast results as a table 
blastFile <- "/scratch/SampleDataFiles/Annotation/transcriptBlast.txt"
keggFile <- "/scratch/SampleDataFiles/Annotation/kegg.txt"
koFile <- "/scratch/SampleDataFiles/Annotation/ko.txt"
blast <- read.table(blastFile, sep="\t", header=FALSE)
# set column names to match fields selected in BLAST 
colnames(blast) <- c("trans","sp","qlen","slen", "bitscore", "length", "nident", "pident", "evalue", "ppos")
# calculate the percentage of identical matches relative to subject length 
blast$cov <- blast$nident/blast$slen
# filter for at least 50% coverage of subject (SwissProt) sequence 
blast <- subset(blast, cov > .5)
# check the blast table 
kable(head(blast))
# Load SwissProt to KEGG as a table
kegg <- read.table(keggFile, sep="\t", header=FALSE)
# Set the Swissprot to KEGG column names
colnames(kegg) <- c("sp", "kegg")
# Remove the up: prefix from sp column
kegg$sp <- gsub("up:", "", kegg$sp)
# Check the kegg table
kable(head(kegg))
# Merge BLAST and SwissProt-to-KEGG
blastKegg <- merge(blast, kegg)
# Check the merged table
kable(head(blastKegg))
# Load KEGG to KO as a table
ko <- read.table(koFile, sep="\t", header=FALSE)
# Set column names
colnames(ko) <- c("kegg", "ko")
# Check the ko table
kable(head(ko))
# Merge KOs
blastKo <- merge(blastKegg, ko)
# Check the blast ko table
kable(head(blastKo))
tx2gene <- unique(subset(blastKo, select=c(trans, ko)))
# Check the tx2gene table
kable(tx2gene)
# Write as a csv file, excluding row.names
write.csv(tx2gene, file="tx2gene.csv", row.names=FALSE)
