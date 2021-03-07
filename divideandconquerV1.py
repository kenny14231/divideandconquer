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

    leftBestArray:list = array[leftBestPosition[0]: leftBestPosition[1]]
    rightBestArray:list = array[rightBestPosition[0]+halfwayPoint: rightBestPosition[1]+halfwayPoint]
    inBetweenArray:list = array[leftBestPosition[1]: rightBestPosition[0]+halfwayPoint]

    #print(f"leftBestArray: {leftBestArray}")
    #print(f"inBetweenArray: {inBetweenArray}")
    #print(f"rightBestArray: {rightBestArray}")

    leftBestSum:int = sum(leftBestArray)
    rightBestSum:int = sum(rightBestArray)
    inBetweenSum:int = sum(inBetweenArray)

    if(leftBestSum >= rightBestSum):
        maxArray = leftBestArray
        if(inBetweenSum + rightBestSum > 0 and rightBestSum > 0):
            #add inbetweensum and rightbestsum to array
            maxArray = maxArray + inBetweenArray + rightBestArray
        elif(inBetweenSum > 0 and rightBestSum < 0):
            #add inbetweensum to array
            maxArray = maxArray + inBetweenArray
    else:
        maxArray = rightBestArray
        if(inBetweenSum + leftBestSum > 0 and leftBestSum > 0):
            #add inbetweensum and rightbestsum to array
            maxArray = leftBestArray + inBetweenArray + maxArray
        elif(inBetweenSum > 0 and rightBestSum < 0):
            #add inbetweensum to array
            maxArray = inBetweenArray + maxArray
    return (maxArray, inBetweenArray)

def main():
    times1 :list = []
    times2:list = []

    listLength :int = 10
    #for size in range(1, 10):
        #arraySize:int = size * 30
    arraySize:int = 100

    for i in range(20):
        newArray :list = createArray(arraySize)
        
        maxSubArray1 = divideAndConquer1(newArray)[0]

        result2 = divideAndConquer2(newArray)
        maxSubArray2 = result2[0]
        inBetweenArray = result2[1]

        if(maxSubArray1 != maxSubArray2):
            print("discrepancy!")
            print(f"newArray: {newArray}")
            print(f"divideAndConquer1 bestArray: {maxSubArray1}")
            print(f"divideAndConquer2 bestArray: {maxSubArray2}")
            print(f"divideAndConquer2 inBetweenArray: {inBetweenArray}")
        #print(f"Are they equivalent? {maxSubArray1 == maxSubArray2}")
        

    for i in range(listLength):
        newArray :list = createArray(arraySize)
        print(f"newArray: {newArray}")

        result1:tuple = divideAndConquer(newArray)
        maxSubArray1 :list = result[0]
        maxSubArraySum1 = sum(maxSubArray)
        print(f"maxSubArray1: {maxSubArray1}")
        print(f"maxSum1: {maxSubArraySum1}")

        timeTaken1 :float = result[1]
        times1.append(timeTaken1)

        result2:tuple = divideAndConquer2(newArray)
        maxSubArray2:list = result2[0]
        maxSubArraySum2 = sum(maxSubArray2)
        print(f"maxSubArray2: {maxSubArray2}")
        print(f"maxSum2: {maxSubArraySum2}")

        timeTaken2 :float = result2[1]
        times2.append(timeTaken2)
        

    averageTime1 :float = sum(times1) / listLength
    #print(f"arraySize: {arraySize}")
    print(f"Average Time 1: {averageTime1}")

    averageTime1 :float = sum(times2) / listLength
    #print(f"arraySize: {arraySize}")
    print(f"Average Time 2: {averageTime2}")

if __name__ == "__main__":
    main()
