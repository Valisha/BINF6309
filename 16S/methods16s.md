author: Valisha Shah title: Variant Calling output: html\_document: toc:
true toc\_depth: 4 toc\_float: true dev: ‘svg’ md\_document: variant:
gfm —

Moving-pictures
===============

Demultiplexing sequences
------------------------

-   the demux emp-single command refers to the fact that these sequences
    are barcoded according to the Earth Microbiome Project protocol, and
    are single-end reads. The demux.qza QIIME 2 artifact will contain
    the demultiplexed sequences. The second output (demux-details.qza)
    presents Golay error correction details, and will not be explored in
    this tutorial (you can visualize these data using qiime metadata
    tabulate).

Sequence quality control and feature table construction
-------------------------------------------------------

### With DADA2

-   The dada2 denoise-single method requires two parameters that are
    used in quality filtering: –p-trim-left m, which trims off the first
    m bases of each sequence, and –p-trunc-len n which truncates each
    sequence at position n. This allows one to remove low quality
    regions of the sequences. Demux.qzv contains the quality reads.

FeatureTable and FeatureData summaries
--------------------------------------

-   The feature-table summarize command will give you information on how
    many sequences are associated with each sample and with each
    feature, histograms of those distributions, and some related summary
    statistics. The feature-table tabulate-seqs command will provide a
    mapping of feature IDs to sequences, and provide links to easily
    BLAST each sequence against the NCBI nt database. The latter
    visualization will be very useful later in the tutorial, when you
    want to learn more about specific features that are important in the
    data set.

Generate a tree for phylogenetic diversity
------------------------------------------

-   analyses QIIME supports several phylogenetic diversity metrics,
    including Faith’s Phylogenetic Diversity and weighted and unweighted
    UniFrac. In addition to counts of features per sample (i.e., the
    data in the FeatureTable\[Frequency\] QIIME 2 artifact), these
    metrics require a rooted phylogenetic tree relating the features to
    one another. This information will be stored in a
    Phylogeny\[Rooted\] QIIME 2 artifact. To generate a phylogenetic
    tree we will use align-to-tree-mafft-fasttree pipeline from the
    q2-phylogeny plugin.

Alpha and beta diversity analysis
---------------------------------

-   QIIME 2’s diversity analyses are available through the q2-diversity
    plugin, which supports computing alpha and beta diversity metrics,
    applying related statistical tests, and generating interactive
    visualizations. We’ll first apply the core-metrics-phylogenetic
    method, which rarefies a FeatureTable\[Frequency\] to a
    user-specified depth, computes several alpha and beta diversity
    metrics, and generates principle coordinates analysis (PCoA) plots
    using Emperor for each of the beta diversity metrics. analyze sample
    composition in the context of categorical metadata using PERMANOVA
    (first described in Anderson (2001)) using the
    beta-group-significance command.

Alpha rarefaction
-----------------

-   plotting we’ll explore alpha diversity as a function of sampling
    depth using the qiime diversity alpha-rarefaction visualizer. This
    visualizer computes one or more alpha diversity metrics at multiple
    sampling depths, in steps between 1 (optionally controlled with
    –p-min-depth) and the value provided as –p-max-depth\#\# Taxonomic
    analysis
-   explore the taxonomic composition of the samples, and again relate
    that to sample metadata. The first step in this process is to assign
    taxonomy to the sequences in our FeatureData\[Sequence\] QIIME 2
    artifact. We’ll do that using a pre-trained Naive Bayes classifier
    and the q2-feature-classifier plugin

Differential abundance testing with ANCOM
-----------------------------------------

-   ANCOM can be applied to identify features that are differentially
    abundant \# Atacama soil microbiome \#\# Paired-end read analysis \*
    demultiplexing the sequence reads requires This requires the sample
    metadata file, and you must indicate which column in that file
    contains the per-sample barcodes
-   After demultiplexing reads, we’ll look at the sequence quality based
    on ten-thousand randomly selected reads, and then denoise the data
