#!/usr/bin/env bash
plink --file hapmap1 
## making a binary PED file
plink --file hapmap1 --make-bed --out hapmap1
## creating a new file that only includes individuals with high genotyping 
plink --file hapmap1 --make-bed --mind 0.05 --out highgeno
## working with binary PED file
plink --bfile hapmap1 --missing --out miss_stat
## analysing the data by chromosome
plink --bfile hapmap1 --chr 1 --out real --missing
plink --bfile hapmap1 --chr 2 --out real --missing
## summary statistics of the allele frequency 
plink --bfile hapmap1 --freq --out freq_stat
plink --bfile hapmap1 --freq --within pop.phe --out freq_stat
## if we are just interested in specfic SNP
plink --bfile hapmap1 --snp rs1891905 --freq --within pop.phe --out snp1_frq_stat
## basic association analysis
plink --bfile hapmap1 --assoc --out as1
## list the association statistics and print the top 10 
sort --key=7 -nr as1.assoc | head 
## To get a sorted list of association results, that also includes a range of significance values that are adjusted for multiple testing, use the --adjust flag
plink --bfile hapmap1 --assoc --adjust --out as2 
plink --bfile hapmap1 --pheno pop.phe --assoc --adjust --out as3
## genotypic and other association models 
plink --bfile hapmap1 --model --snp rs2222162 --out mod1
plink --bfile hapmap1 --model --cell 0 --snp rs2222162 --out mod2
## stratification analysis 
## clustering analysis 
plink --bfile hapmap1 --cluster --mc 2 -- ppc 0.05 --out str1 
## association analysis, accounting for clusters 
plink --bfile hapmap1 --mh --within str1.cluster2 --adjust --out aac1 
## reuquesting for each cluster that contais at least 1 case and 1 control 
plink --bfile hapmap1 --cluster --cc --ppc 0.01 --out version2
plink --bfile hapmap1 --mh --within version2.cluster --adjust --out aac2
plink --bfile hapmap1 --cluster --K 2 --out version3 
## external clustering in the analyses
plink --bfile hapmap1 --mh --within pop.phe --adjust --out aac3
plink --bfile hapmap1 --cluster --matrix --out ibd_view
## Quantitative trait association analysis
plink --bfile hapmap1 --assoc --pheno qt.phe --out quant1
plink --bfile hapmap1 --assoc --pheno qt.phe --perm --within str1.cluster2 --out quant2
# perform the analysis for the main SNP of interest rather than all SNPs 
plink --bfile hapmap1 --pheno qt.phe --gxe --covar pop.phe --snp rs2222162 --out quant3
# extracting a SNP of interest
plink --bfile hapmap1 --snp rs2222162 --recodeAD --out rec_snp1 


