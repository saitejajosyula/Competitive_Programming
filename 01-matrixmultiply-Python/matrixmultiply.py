# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    
    row1 = len(m1)
    row2 = len(m2)
    col1 = len(m1[0])
    col2 = len(m2[0])

    if row2 != col1:

        return None

    
    lis = [[0 for i in range(col2)] for j in range(row1)]

    for i in range(row1):

        for j in range(col2):

            output = 0

            for k in range(col1):

                output = output + m1[i][k] * m2[k][j]
            
            lis[i][j] = output
    
    return lis

    # if col1 == row2:
        
    #     m3 = []
        
    #     for row in range(row1):
            
    #         m3 += [[0]*col2]
        
    # elif col2 == row1:
            
    #         m3 = []
            
    #         for row in range(row2):
                
    #             m3 +=  [[0] * col1]
        
    # rows = len(m3)
    # cols = len(m3[0])

    # for col in range(cols):

    #     collist = []
        
    #     for row in range(rows):
            
    #         collist.append(row)
        
    # return m3;




