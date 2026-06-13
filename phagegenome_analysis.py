from Bio import SeqIO
import pandas as pd
import glob
for file in glob.glob("../AB_Phages_Project/*.fasta"):
	print(file)

files = glob.glob("../AB_Phages_Project/*.fasta")
print("Total files found:", len(files))

results = []

for file in files:
    genome = file.split("/")[-1]
    record = SeqIO.read(file, "fasta")
    seq = str(record.seq).upper()
    length = len(seq)
    gc = (seq.count("G") + seq.count("C")) / length * 100
    results.append([genome, length, round(gc, 2)])

print(results[:3])
