def second_max(nums):
    max_pair = [float("-inf"),float("-inf")]
    for i in nums:
        if i >= max_pair[0]:
            max_pair[1] = max_pair[0]
            max_pair[0] = i
        elif i < max_pair[0] and i >= max_pair[1]:
            max_pair[1] = i
        else:
            continue
        print(max_pair)
    return max_pair[1]


if __name__ == "__main__":
    ans = second_max([1,2,4,5,2,3])
    print(ans)