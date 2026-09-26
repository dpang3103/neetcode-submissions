class Solution:
    def isHappy(self, n: int) -> bool:
        seen_list = []
        x = n

        while x not in seen_list:
            seen_list.append(x)
            x = self.sum_squares(x)
            if x == 1:
                return True
        
        return False

    def sum_squares(self, x: int) -> int:
        return sum(int(d) ** 2 for d in str(x))
