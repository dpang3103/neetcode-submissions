class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        dimension = len(matrix)
        matrix[:] = matrix[::-1]
        for i in range(dimension):
            for j in range(i+1,dimension):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        