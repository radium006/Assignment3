from operations import sum, getLargestNum, getSmallestNum, getEvenNums, getOddNums, printPositiveNums, convertPositiveNums, multiplyList, vectorMultiply

print("Welcome to Kev's list operation program")
print("The purpose of this program is to manipulate and perform mathmatical operations on any given list")

while True:


    array1 = []
    print("Enter 10 positive or negative integers into a list: ")
    elms = 0
    while elms != 10:
        try:
            array1.append(int(input()))
            elms += 1
        except ValueError:
            print("INCORRECT INPUT, TRY AGAIN")    

    print("Your array is:")
    print(array1)

    print("The sum of the elements in the array is "+ str(sum(array1)))
    print("The largest element of the array is " + str(getLargestNum(array1)))
    print("The smallest element of the array is " + str(getSmallestNum(array1)))
    print("The even elements of the array are " + str(getEvenNums(array1)))
    print("The odd elements of the array are " + str(getOddNums(array1)))
    print("The positive elements of the array are " + str(printPositiveNums(array1)))
    print("All of the elements converted to positive: " + str(convertPositiveNums(array1)))
    
    factor = int(input("Enter a factor to multiply elements of the array: "))
    print("The elements multipled by the inputed factor are: " + str(multiplyList(array1, factor)))
    #print(vectorMultiply(testArray,testArray2))

    cont = input("Would you like to continue? Press 'q' to exit program or any key to continue: ")
    if cont == 'q':
        break