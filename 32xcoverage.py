# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below
import sys
#create list of nucleotides
#maybe sys argv loop has to go here instead?
import random
genome_length = int(sys.argv[1])
seq_length = int(sys.argv[2])
genome = [0] *genome_length
read_number = int(sys.argv[3])

for i in range(read_number):
    start = random.randint(0,(genome_length-seq_length))
    for j in range(seq_length):
        genome[start+j] += 1
        
print(min(genome[seq_length:genome_length-seq_length]),max(genome[seq_length:genome_length-seq_length]),(sum(genome[seq_length:genome_length-seq_length])/genome_length))

#calculate min + max within range 100-900
#use sys.argv and values in terminal  

    
    
#print(genome)
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
