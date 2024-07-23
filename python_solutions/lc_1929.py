# https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_l = len(nums)
        ans = [None] * (2*nums_l)
        for i in range(0,nums_l):
            ans[i] = nums[i]
            ans[i+nums_l] = nums[i]
        
        return ans