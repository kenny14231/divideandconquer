from random import *
from math import *
import time

def createArray(length:int):
    newArray :list = []
    for i in range(length):
        num :int = randint(-10, 10)
        newArray.append(num)
    return newArray

def sum(array:list):
    sum = 0
    for number in array:
        sum += number
    return sum

def divideAndConquer1(array:list):
    startTime :float = time.perf_counter()
    arrayLength :int = len(array)
    maxNum = -100
    maxPosition :list = [0,0]
    for startIndex in range(arrayLength):
        for endIndex in range(startIndex + 1, arrayLength + 1):
            #print(f"start index: {startIndex} end index: {endIndex}")
            #print(array[startIndex:endIndex])
            subArray :list = array[startIndex:endIndex]
            arraySum :int = sum(subArray)

            position :list = [startIndex, endIndex]
            #print(f"subArray: {subArray}")
            #print(f"arraySum: {arraySum}")

            if(arraySum > maxNum):
                maxNum = arraySum
                maxPosition = position

    maxStartIndex :int = maxPosition[0]
    maxEndIndex :int = maxPosition[1]
    maxArray :list = array[maxStartIndex:maxEndIndex]
    endTime = time.perf_counter()
    #print(f"time taken: {endTime - startTime} seconds")
    return (maxArray, endTime - startTime)

def divideAndConquerIndex(array:list):
    #startTime :float = time.perf_counter()
    arrayLength :int = len(array)
    maxNum = -100
    maxPosition :list = [0,0]
    for startIndex in range(arrayLength):
        for endIndex in range(startIndex + 1, arrayLength + 1):
            #print(f"start index: {startIndex} end index: {endIndex}")
            #print(array[startIndex:endIndex])
            subArray :list = array[startIndex:endIndex]
            arraySum :int = sum(subArray)

            position :list = [startIndex, endIndex]
            #print(f"subArray: {subArray}")
            #print(f"arraySum: {arraySum}")

            if(arraySum > maxNum):
                maxNum = arraySum
                maxPosition = position

    #maxStartIndex :int = maxPosition[0]
    #maxEndIndex :int = maxPosition[1]
    #maxArray :list = array[maxStartIndex:maxEndIndex]
    #endTime = time.perf_counter()
    #print(f"time taken: {endTime - startTime} seconds")
    return (maxPosition)

def divideAndConquer2(array:list):
    startTime:float = time.perf_counter()
    arrayLength:int = len(array)
    halfwayPoint:int = floor(arrayLength/2)
    maxArray:list = []
    leftArray:list = array[:halfwayPoint]
    rightArray:list = array[halfwayPoint:]
    
    #print(leftArray)
    #print(rightArray)

    leftBestPosition:list = divideAndConquerIndex(leftArray)
    rightBestPosition:list = divideAndConquerIndex(rightArray)

    newArray:list = array[leftBestPosition[0]:rightBestPosition[1]+halfwayPoint]
    maxArrayPosition:list = divideAndConquerIndex(newArray)
    maxArray:list = newArray[maxArrayPosition[0]:maxArrayPosition[1]]

    return (maxArray, newArray, rightArray)

def main():
    times1 :list = []
    times2:list = []

    listLength :int = 10
    #for size in range(1, 10):
        #arraySize:int = size * 30
    arraySize:int = 100
    allGood = True

    for i in range(100):
        newArray :list = createArray(arraySize)
        
        maxSubArray1 = divideAndConquer1(newArray)[0]

        result2 = divideAndConquer2(newArray)
        maxSubArray2 = result2[0]
        cutArray = result2[1]
        rightArray = result2[2]

        
        
        if(maxSubArray1 != maxSubArray2):
            allGood = False
            print("discrepancy!")
            print(f"newArray: {newArray}")
            print(f"divideAndConquer1 bestArray: {maxSubArray1}")
            print(f"divideAndConquer2 bestArray: {maxSubArray2}")
            print(f"divideAndConquer2 cutArray: {cutArray}")
            print(f"divideAndConquer2 rightArray: {rightArray}")
            print("\n")

    print(f"allGood: {allGood}")
        #print(f"Are they equivalent? {maxSubArray1 == maxSubArray2}")
       

if __name__ == "__main__":
    main()
