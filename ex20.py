def pairSum(a, sum):
    return [s for i in range(len(a)) if (s := str(a[i]) + '+' + str(sum - a[i])) and (int(sum - a[i]) in a[i:])]
    

print(pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))
