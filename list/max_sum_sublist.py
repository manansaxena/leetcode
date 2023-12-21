def max_sum_sublist(nums):
    if len(nums) == 1:
            return nums[0]
    max_sum = -2**32
    curr_sum = 0
    for i in nums:
        curr_sum = curr_sum + i
        if i >= curr_sum:
            curr_sum = i
        if max_sum <= curr_sum:
            max_sum = curr_sum
    return max_sum