# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointer approach - slow fast
        if len(nums) == 0:
            return 0
        slow = 0
        fast = 0
        for i in range(0,len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow