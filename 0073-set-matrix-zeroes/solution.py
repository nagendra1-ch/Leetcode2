import numpy as np
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zr, zc = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zr.add(i)
                    zc.add(j)
    
        for i in zr:
            for j in range(n):
                matrix[i][j] = 0

        for j in zc:
            for i in range(m):
                matrix[i][j] = 0

