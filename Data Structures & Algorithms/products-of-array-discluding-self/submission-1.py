class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]*nums[i])
        for i in range(1,len(nums)):
            suffix.append(suffix[i-1]*nums[-1-i])
        suffix.reverse()
        output = [suffix[1]]
        for i in range(1,len(nums)-1):
            output.append(prefix[i-1]*suffix[i+1])
        output.append(prefix[-2])
        return output

        # product = 1
        # for num in nums:
        #     product *= num
        # output = [product] * len(nums)
        # for i in range(len(nums)):
        #     if output[i] != 0:
        #         output[i] = int(output[i]/nums[i])
        # return output


