def find_product(lst):
    prod = 1
    prod_0 = 1
    num_zeros = lst.count(0)

    for i in lst:
        if num_zeros == 1 and i != 0:
            prod_0 *= i
        prod *= i
    
    for i in range(0,len(lst)):
        if lst[i] == 0 :
            if num_zeros == 1:
                lst[i] = prod_0
            else :
                lst[i] = prod
        else:
            lst[i] = prod / lst[i]
    
    return lst

if __name__ == "__main__":
    ans = find_product([1,2,0,0])
    print(ans)