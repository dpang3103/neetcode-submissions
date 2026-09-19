class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            remaining = target - num
            rest_of_nums = nums[nums.index(num)+1:]
            if remaining in rest_of_nums:
                return [nums.index(num),rest_of_nums.index(remaining)+nums.index(num)+1]