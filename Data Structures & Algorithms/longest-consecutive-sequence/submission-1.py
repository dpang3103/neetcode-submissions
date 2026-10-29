

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ordered_nums = set(nums)

        starting_nums = []
        for num in ordered_nums:
            if num - 1 not in ordered_nums:
                starting_nums.append(num)

        max_count = 0
        for num in starting_nums:
            seq = 1
            while num + 1 in ordered_nums:
                seq += 1
                num += 1
            if seq > max_count:
                max_count = seq
        return max_count
