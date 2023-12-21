def max_min(lst):
    # Write your code here
    min_pointer = 0
    max_pointer = len(lst) - 1
    flag = "max"
    res = []
    while min_pointer <= max_pointer:
        if flag == "max":
            res.append(lst[max_pointer])
            max_pointer -= 1
            flag = "min"
        else:
            res.append(lst[min_pointer])
            min_pointer += 1
            flag = "max"
    return res

if __name__ == "__main__":
    res = max_min([1,2,3,4,5,6,7])
    print(res)