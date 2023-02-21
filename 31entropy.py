# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input
import sys
import math
p_i = []

try:
    i = 0
    while i < len(sys.argv)-1:
        p_i.append(float(sys.argv[i+1])*math.log2(float(sys.argv[i+1])))
        i += 1
    h = (sum(p_i)) - (2*sum(p_i))
    print(f'{h:.3f}')
except:
    print("nope")
#p_x_in = 0
#for val in sys.argv[1:]:
    #try p_x.append(float(val))
       # except sys.argv == str:
            #break
#print(p_x)


#H = -sum(p_x*math.log2(p_x))
#print(H)

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
