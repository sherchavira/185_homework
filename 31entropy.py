# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input
genome_len = 1000
seq_len = 100
nts = ['A','C','G','T']
genome = []
for nt in genome_len:
    genome.append(nts)
print(genome)


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
