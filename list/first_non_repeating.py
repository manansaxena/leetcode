def first_non_repeating(nums):
    ans = 0
    for i in nums:
        if nums.count(i) == 1:
            return i
    
    return -1






if __name__ == "__main__":
    ans = first_non_repeating([1,2,3,4,2,1])
    print(ans)