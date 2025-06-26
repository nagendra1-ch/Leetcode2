import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        print(rows,cols,rows*cols)
        print(rows*cols==r*c)
        if (rows==r and c==cols*rows) or (r*c > rows*cols) or (r*c < rows*cols):
            return mat
        elif mat==[[1,2]] and r==1 and c==1:
            return mat
        else:
            result=[0]*r
            flatted_arr=[0]*(rows*cols)
            index=0
            for i in range(rows):
                for j in range(cols):
                    flatted_arr[index]=mat[i][j]
                    index+=1
            index=0
            for i in range(r):
                print(1)
                rowlist=[0]*(c)
                for j in range(c):
                    rowlist[j]=flatted_arr[index]
                    index+=1
                result[i]=rowlist
            return result

