class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_checker = set()
        for num in nums:
            if num in duplicate_checker:
                return True
            else:
                duplicate_checker.add(num)
        return False 