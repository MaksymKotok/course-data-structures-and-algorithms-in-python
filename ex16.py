def sumDiagonal(a):
    return sum([a[i][i] for i in range(len(a))])


myList = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(sumDiagonal(myList))