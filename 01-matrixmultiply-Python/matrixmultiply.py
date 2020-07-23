# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.

import numpy as np

def fun_matrixmultiply(m1, m2):

    if len(m2) != len(m1[0]):
        return None
    
    lis = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]

    for i in range(len(m1)):

        for j in range(len(m2[0])):

            output = 0

            for k in range(len(m1[0])):

                output = output + m1[i][k] * m2[k][j]
            
            lis[i][j] = output
    
    return lis




