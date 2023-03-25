# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use 20 named variables
# Variation: use a list

#import the file?
#print out 20 letters to indicate what aa they are on
#what other values are needed?

import gzip
import sys
prot_bank = "ACDEFGHIKLMNPQRSTVWY"
prot_count = [0]*20
def composition(prot):
	tally = [0]*20
	
	tally[0] = prot.count('A')
	tally[1] = prot.count('C')
	tally[2] = prot.count('D')
	tally[3] = prot.count('E')
	tally[4] = prot.count('F')
	tally[5] = prot.count('G')
	tally[6] = prot.count('H')
	tally[7] = prot.count('I')
	tally[8] = prot.count('K')
	tally[9] = prot.count('L')
	tally[10] = prot.count('M')
	tally[11] = prot.count('N')
	tally[12] = prot.count('P')
	tally[13] = prot.count('Q')
	tally[14] = prot.count('R')
	tally[15] = prot.count('S')
	tally[16] = prot.count('T')
	tally[17] = prot.count('V')
	tally[18] = prot.count('W')
	tally[19] = prot.count('Y')
	return tally
with gzip.open(sys.argv[1], 'rt') as fp:
	while True:
		line = fp.readline()
		if line == '': break
		if line.startswith('>'): continue
		for i in range(len(prot_bank)):
			for aaline in line:
				if aaline == prot_bank[i]:
					prot_count[i] += 1
					

for j in range(len(prot_bank)):
	print(prot_bank[j],prot_count[j],f"{prot_count[j]/sum(prot_count):.4f}")
"""

#count = 0
#for p in aa:
	#chang position
	#if #file? = aa
		#count += 1
"""
"""


tally = [0]*20
for aa in range(len(aas)):
	for aaline in line:
			if aaline == aas[aa]:
				tally[aa] += 1
for i in range(len(tally)):
	print(aas[i], tally[i], tally[i]/sum(tally))
"""



"""
i = 0
while i in range(0, len(aa[0]):
	print(aa[0][i], aa[2][i], aa[1][i])
	i += 1

#print slices of AA
#have python run through the file and search for AAs?
#return specific AA, look for AA, print position, add to count


"""
"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""
