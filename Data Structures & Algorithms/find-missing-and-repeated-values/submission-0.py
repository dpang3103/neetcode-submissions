class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        unique_numbers = set()
        total_numbers = len(grid[0])**2
        total_value = total_numbers*(total_numbers+1)/2
        grid_total = 0
        a = 0

        for row in grid:
            for column in row:
                if column in unique_numbers:
                    a = column
                unique_numbers.add(column)
                grid_total += column
        
        b = int(total_value - grid_total + a)
        return [a, b]

        

        