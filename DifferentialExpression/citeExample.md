author: Valisha Shah (Valisha) output: html\_document: toc: true
toc\_depth: 4 toc\_float: true dev: ‘svg’ md\_document: variant: gfm
bibliography: bibliography.ris \_\_\_

Overview
--------

The two main steps in performing differential expression analysis are to
estimate the relative abundance of transcripts, and to apply statistical
models to test for differential expression between treatment groups.
Estimating relative abundance is basically determining how many NGS
reads match a given gene within a genome. In this module I used Salmon
\[@Patro\] to estimate relative abundance, tximport \[@Soneson\] to
import the Salmon abundance estimates, and DESeq2 \[@Love\] to perform
statistical tests to identify differentially expressed genes.

References
----------

1.  Love, Michael I., Wolfgang Huber, and Simon Anders. 2014. “Moderated
    Estimation of Fold Change and Dispersion for RNA-Seq Data with
    DESeq2.” *Genome Biol* 15 (12): 550–50..
2.  Patro, Rob, Geet Duggal, Michael I. Love, Rafael A. Irizarry, and
    Carl Kingsford. 2017. “Salmon Provides Fast and Bias-Aware
    Quantification of Transcript Expression.” *Nat Methods* 14 (4):
    417–19..
3.  Soneson, Charlotte, Michael I. Love, and Mark D. Robinson. 2016.
    “Differential Analyses for RNA-Seq: Transcript-Level Estimates
    Improve Gene-Level Inferences.” *F1000Res* 4 (February): 1521–1..
