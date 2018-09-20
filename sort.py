print("Welcome to Kev's Sort program")

def bubbleSort(arr):
    for i in reversed(range(len(arr))):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr [j+1] = arr[j+1], arr[j]
        
    return arr    

def rbubbleSort(arr):
    for i in reversed(range(len(arr))):
        for j in range(0, i):
            if arr[j] < arr[j+1]:
                arr[j], arr [j+1] = arr[j+1], arr[j]
        
    return arr 



myArr = [8, 9, 5, 2, 7, 56, 90, 50, 1, 0, 3, ]
#print('****************************************')
print('Unsorted Array')
print(myArr)
#print('****************************************')

print("Sorting Array in acsending order using bubble sort....")
print(bubbleSort(myArr))
    
print("Sorting Array in decsending order using bubble sort....")
print(rbubbleSort(myArr))

    