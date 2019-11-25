PLINK tutorial results
================
Valisha Shah

``` r
library(knitr)
library(readr)
```

``` r
# the snp1_frq_strat files contains the population-specfic frequencies for this single SNP, which is rs1891905 for this file 
kable(head(read.table("snp1_frq_stat.frq.strat")))
```

| V1  | V2        | V3   | V4 | V5 | V6     | V7  | V8      |
| :-- | :-------- | :--- | :- | :- | :----- | :-- | :------ |
| CHR | SNP       | CLST | A1 | A2 | MAF    | MAC | NCHROBS |
| 1   | rs1891905 | 1    | 1  | 2  | 0.4111 | 37  | 90      |
| 1   | rs1891905 | 2    | 1  | 2  | 0.3977 | 35  | 88      |

``` r
# we can see the frequency distribution between Chinese and Japansese individuals 
kable(head(read.table("as3.assoc.adjusted")))
```

| V1  | V2         | V3        | V4        | V5       | V6       | V7        | V8        | V9       | V10     |
| :-- | :--------- | :-------- | :-------- | :------- | :------- | :-------- | :-------- | :------- | :------ |
| CHR | SNP        | UNADJ     | GC        | BONF     | HOLM     | SIDAK\_SS | SIDAK\_SD | FDR\_BH  | FDR\_BY |
| 8   | rs2585179  | 2.694e-08 | 3.216e-05 | 0.001852 | 0.001852 | 0.00185   | 0.00185   | 0.001852 | 0.02169 |
| 11  | rs10768140 | 6.778e-08 | 5.448e-05 | 0.004658 | 0.004658 | 0.004647  | 0.004647  | 0.002329 | 0.02728 |
| 15  | rs4468542  | 1.154e-07 | 7.386e-05 | 0.007931 | 0.00793  | 0.007899  | 0.007899  | 0.002644 | 0.03097 |
| 6   | rs372440   | 6.924e-07 | 0.0002061 | 0.04759  | 0.04758  | 0.04647   | 0.04647   | 0.01082  | 0.1268  |
| 6   | rs9395476  | 1.102e-06 | 0.0002692 | 0.07577  | 0.07576  | 0.07297   | 0.07296   | 0.01082  | 0.1268  |

``` r
# we see a pre-sorted list of association results. In this particular case, we see that no single variant is significant at the 0.05 level after the genome-wide correction. 
kable(head(read.table("as2.assoc.adjusted")))
```

| V1  | V2         | V3        | V4        | V5     | V6     | V7        | V8        | V9      | V10     |
| :-- | :--------- | :-------- | :-------- | :----- | :----- | :-------- | :-------- | :------ | :------ |
| CHR | SNP        | UNADJ     | GC        | BONF   | HOLM   | SIDAK\_SS | SIDAK\_SD | FDR\_BH | FDR\_BY |
| 13  | rs9585021  | 5.586e-06 | 4.994e-05 | 0.3839 | 0.3839 | 0.3188    | 0.3188    | 0.09719 | 1       |
| 2   | rs2222162  | 5.918e-06 | 5.232e-05 | 0.4068 | 0.4067 | 0.3342    | 0.3342    | 0.09719 | 1       |
| 9   | rs10810856 | 7.723e-06 | 6.483e-05 | 0.5308 | 0.5308 | 0.4118    | 0.4118    | 0.09719 | 1       |
| 2   | rs4675607  | 8.05e-06  | 6.703e-05 | 0.5533 | 0.5533 | 0.4249    | 0.4249    | 0.09719 | 1       |
| 2   | rs4673349  | 8.485e-06 | 6.994e-05 | 0.5832 | 0.5831 | 0.4419    | 0.4419    | 0.09719 | 1       |

``` r
# after performing the matching based on the genome-wide IBS, we can perform the association test conditional on the matching. for this we use the Cochran-Man
# tel-Haenszel association statistic, which tests for SNP-disease conditional on
# the clustering supplied by the clusterr file.

kable(head(read.table("aac3.cmh.adjusted")))
```

| V1  | V2        | V3        | V4        | V5        | V6        | V7        | V8        | V9        | V10       |
| :-- | :-------- | :-------- | :-------- | :-------- | :-------- | :-------- | :-------- | :-------- | :-------- |
| CHR | SNP       | UNADJ     | GC        | BONF      | HOLM      | SIDAK\_SS | SIDAK\_SD | FDR\_BH   | FDR\_BY   |
| 2   | rs2222162 | 2.594e-10 | 2.594e-10 | 1.783e-05 | 1.783e-05 | 1.783e-05 | 1.783e-05 | 1.783e-05 | 0.0002089 |
| 2   | rs4675607 | 4.03e-06  | 4.03e-06  | 0.277     | 0.277     | 0.2419    | 0.2419    | 0.1385    | 1         |
| 2   | rs4673349 | 1.204e-05 | 1.204e-05 | 0.8276    | 0.8276    | 0.5629    | 0.5629    | 0.1679    | 1         |
| 2   | rs1375352 | 1.204e-05 | 1.204e-05 | 0.8276    | 0.8276    | 0.5629    | 0.5629    | 0.1679    | 1         |
| 13  | rs9585021 | 1.222e-05 | 1.222e-05 | 0.8395    | 0.8395    | 0.5681    | 0.5681    | 0.1679    | 1         |

``` r
# this is where we analyze the quantitative trait directly that is a disease trait is based on a simple median split of a quantitative trait 
# the output shows the number of non-missing individuals in each category along with the regression coefficient and standard error, followed by a test of whether these two regression coefficients are signficantly different
kable(head(read.table("quant3.qassoc.gxe")))
```

| V1  | V2        | V3     | V4      | V5     | V6     | V7      | V8     | V9       | V10    |
| :-- | :-------- | :----- | :------ | :----- | :----- | :------ | :----- | :------- | :----- |
| CHR | SNP       | NMISS1 | BETA1   | SE1    | NMISS2 | BETA2   | SE2    | Z\_GXE   | P\_GXE |
| 2   | rs2222162 | 45     | \-2.271 | 0.2245 | 44     | \-1.997 | 0.1722 | \-0.9677 | 0.3332 |

``` r
# viewing the graph on R
m <- as.matrix(read.table("ibd_view.mibs"))
mds <- cmdscale(as.dist(1-m))
k <- c(rep("green",45), rep("blue", 44))
plot(mds, pch=20,col=k)
```

![](runPlink1_files/figure-gfm/unnamed-chunk-2-1.png)<!-- -->

``` r
# Extracting SNP of interest
d <- kable(head(read.table("rec_snp1.raw", header = T)))
#summary(glm(PHENOTYPE~1 ~ rs2222162_A, data = d, family = "binomial"))
```
