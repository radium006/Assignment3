def sum(arr): #function adds each element and returns sum
    total = 0
    for i in range(len(arr)):
        total = total + arr[i]
    return total

def getLargestNum(arr):
    largest = 0
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

def getSmallestNum(arr):
    smallest = getLargestNum(arr)
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

def getEvenNums(arr):
    evenArr = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            evenArr.append(arr[i])
    return evenArr

def getOddNums(arr):
    oddArr = []
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            oddArr.append(arr[i])
    return oddArr

def printPositiveNums(arr):
    posArr = []
    for i in range(len(arr)):
        if arr[i] >= 0:
            posArr.append(arr[i])
    return posArr

def convertPositiveNums(arr):
    posArr = []
    for i in range(len(arr)):
        if arr[i] >= 0:
            posArr.append(arr[i])
        else:
            #arr[i] = arr[i] * -1
            posArr.append(arr[i]* -1)
        
    return posArr

def multiplyList(arr, factor):
    print(arr)
    newArr = []
    for i in range(len(arr)):
        #print(arr[i], factor)
        newArr.append(arr[i] * factor)
    return newArr

def vectorMultiply(arr1, arr2):
    newArr = []
    for i in range(len(arr1)):
        newArr.append(arr1[i] * arr2[i])
    return newArr
