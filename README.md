# Single cell transcriptomic analysis of spinal Dmrt3 neurons in zebrafish and mouse identifies distinct subtypes and reveal novel subpopulations within the dI6 domain

## Sequencing pipeline
We used a snakemake pipeline to download the reference genomes, merging with manually added genes, running the genome indexing, alinging the reads, producing QC and creating the count matrices. Clone this repository and add the raw data files that can be found at GEO accession: **GSE185731** under the folder rawdata. Modify the snakemake pipeline to propperly select the species and well for each file.


## scRNA-seq analysis
The full analysis of the scRNA-seq data is performed in the jupyter notebook under the scRNA-seq analysis folder
