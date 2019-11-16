#!/usr/bin/env bash
#plink --file hapmap1 
# making a binary PED file
plink --file hapmap1 --make-bed --out hapmap1
# creating a new file that only includes individuals with high genotyping 
plink --file hapmap1 --make-bed --mind 0.05 --out highgeno
