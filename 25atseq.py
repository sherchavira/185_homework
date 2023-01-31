# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers
import random
length = 30
count = 0
string = ''
for r in range(length):
	r=random.choice('AAATTTCCGG')
	#print(r,end='')
	string += r
	if r == 'A' or r == 'T':
		count += 1
print(length,(count/length),string)

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
