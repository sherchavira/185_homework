# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import sys
days = int(sys.argv[1])
range_p = int(sys.argv[1])-int(sys.argv[2])
people = int(sys.argv[2])

days_fac = 1
p_fac = 1
for i in range(1, days):
    days_fac = days_fac*i
for j in range(1, range_p):
    p_fac = p_fac*j

V_nr = days_fac/p_fac
V_t = days**people

probability = V_nr/V_t
print(f'{probability:.3f}')

"""
python3 33birthday.py 365 23
0.571
"""

