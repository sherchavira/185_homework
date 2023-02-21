# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys
import sys
numbers = []
for val in sys.argv[1:]:
    numbers.append(int(val))


print(f'minimum: {min(numbers):.1f}')
print(f'maximum: {max(numbers):.1f}')
mean = sum(numbers)/len(numbers)
print(f'mean: {mean:.3f}')
count = len(numbers)
print(f'Count: {count}')
sum_std = 0
for i in range(0, len(numbers)):
    sum_std += (numbers[i]-mean)**2
std_dev = (sum_std/(len(numbers)))**0.5
print(f'std. dev: {std_dev:.3f}')

numbers.sort()
if len(numbers)%2 == 1:
    median = numbers[len(numbers)//2]
else:
    median = (numbers[(len(numbers)//2)-1]+numbers[len(numbers)//2])/2
print(f'Median:{median:.3f}')
print(numbers)
"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
