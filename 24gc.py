# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
count = 0
for c in dna:
	if c == 'C' or c == 'G':
		count += 1
print(f"{count/len(dna):.2f}")
"""
python3 24gc.py
0.42
"""
