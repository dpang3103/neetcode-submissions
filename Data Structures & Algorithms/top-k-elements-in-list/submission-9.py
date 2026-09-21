class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
                counts[num] = counts.get(num,0) + 1
        sorted_counts = sorted(counts, key=lambda num: counts[num], reverse=True)

        return sorted_counts[:k]