def missingNumber(a, count):
    d = []
    for i in range(len(a) - 1):
        d.append(a[i + 1] - a[i])
    _min = min(d)
    lost = []
    for i in range(len(d)):
        if d[i] > _min:
            k = (d[i] // _min) - 1
            for j in range(k):
                lost.append(a[i] + (j + 1) * _min)
    return lost


print(missingNumber([1, 2, 3, 4, 6, 10, 20], 6))
