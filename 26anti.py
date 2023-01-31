# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
string = ''
rdna = dna[::-1]
for nt in rdna:
	if nt == 'A':
		r = 'T'
	elif nt == 'C':
		r = 'G'
	elif nt == 'G':
		r = 'C'
	elif nt == 'T':
		r = 'A'
	string += r
print(string)

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
