def rotate(nums,k):
    if len(nums) == 0:
            return nums
    rotate_by = k % len(nums)
    left_lst = nums[0:len(nums)-rotate_by]
    right_lst = nums[len(nums)-rotate_by:]
    nums[0:len(right_lst)] = right_lst
    nums[len(right_lst):] = left_lst

    return nums


if __name__ == "__main__":
    res = rotate([1,2,3,4,5],2)
    print(res)