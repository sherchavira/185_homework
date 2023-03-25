# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N
#move forward past window after replacing with N
# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import mcb185
import math
import sys


def freq_nt(dna_seq):
	a = dna_seq.count('A')/len(dna_seq)
	c = dna_seq.count('C')/len(dna_seq)
	g = dna_seq.count('G')/len(dna_seq)
	t = dna_seq.count('T')/len(dna_seq)
	return a,c,g,t	
	
def SH_entropy(seq):
	p = freq_nt(seq)
	h = 0
	for i in range(len(freq_nt(seq))):
		if p[i] != 0:
			h -= p[i] * math.log2(p[i])
	return h
w = 11
t = 1.4

for name,seq in mcb185.read_fasta(sys.argv[1]):
	out_seq = list(seq.split())
	for i in range(len(out_seq) - w +1):
		if 'N' in out_seq[i:i+w]: continue
		if SH_entropy(out_seq) < t:
			for j in range(len(seq[i:i+w])):
				seq[j] = 'N'
		print(name, seq)
		#print(win,SH_entropy(win))
#print(file,size_w, entropy)
#convert to fasta
#calculate entropy?
#random fake sequences


"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
