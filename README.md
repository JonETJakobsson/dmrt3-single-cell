# Single cell transcriptomic analysis of spinal Dmrt3 neurons in zebrafish and mouse identifies distinct subtypes and reveal novel subpopulations within the dI6 domain

## Sequencing pipeline
We used a snakemake pipeline to download the reference genomes, merging with manually added genes, running the genome indexing, alinging the reads, producing QC and creating the count matrices. Clone this repository and add the raw data files that can be found at GEO accession: **GSE185731** under the folder rawdata. Modify the snakemake pipeline to propperly select the species and well for each file.
![snakemake pipeline](https://github.com/JonETJakobsson/dmrt3-single-cell/blob/main/Sequencing_pipeline/rule_graph.png)


## scRNA-seq analysis
If you only want to analyse the scRNA-seq data, these can be found as .loom files under Analysis pipeline/data. named: drerio.loom and mmusculus.loom.
The full analysis of the scRNA-seq data is performed in the [jupyter notebook](https://github.com/JonETJakobsson/dmrt3-single-cell/blob/main/Analysis_pipeline/210909_Final_run.ipynb). 
