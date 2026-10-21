from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows 
        for row in board:
            duplicate_checker = []
            for num in row:
                if num == ".":
                    continue
                if num not in duplicate_checker:
                    duplicate_checker.append(num)
                else: 
                    print("row check")
                    return False
        # Check columns 
        for col in range(len(board)):
            column_checker = []
            for row in range(len(board)):
                val = board[row][col]
                if val == ".":
                    continue
                if val not in column_checker:
                    column_checker.append(val)
                else:
                    print("col check")
                    return False
        # Check boxes
        box_checker = defaultdict(set)
        for row in range(len(board)):
            
            for col in range(len(board)):
                val = board[row][col]
                box = (row//3, col//3)
                if val == ".":
                    continue
                if val not in box_checker[box]:
                    box_checker[box].add(val)
                else:
                    print("box check")
                    return False

        return True