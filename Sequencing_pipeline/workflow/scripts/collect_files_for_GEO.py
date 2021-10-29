import os
import shutil
import pandas as pd
import hashlib


path = "D:/dmrt3_sequencing/resources/rawdata/"
os.mkdir(path+"to_GEO")
species = ["drerio", "mmusculus"]
wells = os.listdir(path+species[0])
records = []
for s in species:
    for well in wells:
        src = path+s+"/"+well+"/"+well+"_R1.fastq"
        dst = path+"to_GEO/"+s+"_"+well+".fastq"
        shutil.copyfile(src, dst)
        with open(dst, "rb") as f:
            b = f.read()
            print("file is read")
            hashvalue = hashlib.md5(b).hexdigest()
            print(hashvalue)
        records.append([s+"_"+well, s+"_"+well+".fastq", s, well, hashvalue])
        print(records[-1])


df = pd.DataFrame(records, columns=["sample_name","file", "species", "well", "hash"])
df.to_csv(path+"to_GEO/summary2.csv")