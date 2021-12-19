# Python >= 3.8
def firstSecond(a):
    return [max(a), max([j for i in a if (j := i) is not max(a)])]


myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(firstSecond(myList))
