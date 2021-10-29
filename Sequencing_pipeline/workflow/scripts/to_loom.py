#!/usr/bin/env python
# coding: utf-8

import scanpy as sc
import pandas as pd
import numpy as np

# Load in count and velocyto data
featurecounts = pd.read_table(snakemake.input.counts, sep="\t", skiprows=1)
velocyto = sc.read_loom(snakemake.input.velocyto, sparse=False)

# Get data to make a count (X) and RPKM layer
obs = featurecounts.columns[6:]
var = list(featurecounts["Geneid"])
counts = featurecounts[obs].values
obs = [well.split("/")[3] for well in obs] # fix observation names to wells
gene_length = featurecounts.Length


#calculate RPKM values
RPM_scale = np.sum(counts, axis=0)/1000000 # number of milion reads in well
RPM = counts/RPM_scale
Kbp = gene_length/1000 # gene lengh in Kbp
RPKM = np.apply_along_axis(lambda x: x/Kbp, 0, RPM) # divide KPM with Kbp for each gene

# Add RPKM values to to a layer, and instantiate X with raw counts
adata = sc.AnnData(X=counts.T, layers={"RPKM": RPKM.T})
adata.var_names = var
adata.obs_names = obs
adata.obs["well"] = obs
adata.var["gene_lenght"] = gene_length.values
adata.var["Chromosome"] = featurecounts.Chr.values
# Store location of first exon only
adata.var["Chromosome"] = [exons.split(";")[0] for exons in adata.var["Chromosome"]]

# Arrange adata to the same order as velocyto and transfer gene symbols
adata = adata[:,velocyto.var["Accession"]].copy()
adata.var_names = velocyto.var_names
adata.var["Accession"] = velocyto.var["Accession"]


# Add layers to adata
adata.layers["unspliced"] = velocyto.layers["unspliced"]
adata.layers["spliced"] = velocyto.layers["spliced"]
adata.layers["matrix"] = velocyto.layers["matrix"]

# Output finnished loomfile
adata.write_loom(snakemake.output.loom)
