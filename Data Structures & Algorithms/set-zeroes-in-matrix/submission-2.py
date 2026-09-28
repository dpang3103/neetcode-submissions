class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i] = [x if x == 0 else True for x in matrix[i]]
                    for k in range(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = True
        
        for i in range(n):
            for j in range(m):
                if isinstance(matrix[i][j], bool):
                    matrix[i][j] = 0

        