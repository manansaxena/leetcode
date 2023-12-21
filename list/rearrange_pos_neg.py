def rearrange(lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        if lst[end] >= 0:
            end -= 1
        elif lst[start] < 0:
            start += 1
        else :
            temp = lst[start]
            lst[start] = lst[end]
            lst[end] = temp
            start += 1
            end -= 1
    
    return lst

if __name__ == "__main__":
    res = rearrange([1,3,-1,4,-5])
    print(res)