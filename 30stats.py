# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys
import sys
numbers = [1,2,3,4,5]
print(numbers, f'minimum: {min(numbers)}', f'maximum: {max(numbers)}')
mean = sum(numbers)/len(numbers)
print(f'mean: {mean}')
count = len(numbers)
print(count)
sum_std = 0
for i in range(0, len(numbers)):
    sum_std += (numbers[i]-mean)**2
std_dev = (sum_std/(len(numbers)-1))**0.5
print(f'std. dev: {std_dev}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
