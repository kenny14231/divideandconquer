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
    leftArray:list = array[:halfwayPoint]
    rightArray:list = array[halfwayPoint:]
    
    #print(leftArray)
    #print(rightArray)

    leftBestPosition:list = divideAndConquerIndex(leftArray)
    rightBestPosition:list = divideAndConquerIndex(rightArray)

    newArray:list = array[leftBestPosition[0]:rightBestPosition[1]+halfwayPoint]
    maxArrayPosition:list = divideAndConquerIndex(newArray)
    maxArray:list = newArray[maxArrayPosition[0]:maxArrayPosition[1]]
    endTime = time.perf_counter()

    return (maxArray, endTime-startTime)

def split(array:list):
    arrayLength:int = len(array)
    halfwayPoint:int = floor(arrayLength/2)
    leftArray:list = array[:halfwayPoint]
    rightArray:list = array[halfwayPoint:]
    return (leftArray, rightArray)

def divideAndConquer3(array:list):
    startTime:float = time.perf_counter()

    halfwayPoint = floor(len(array)/2)

    splitArray:tuple = split(array)

    #left side
    leftArray:list = splitArray[0]
    leftArrayLength = len(leftArray)
    leftHalfwayPoint = floor(leftArrayLength/2)

    splitLeftArray:tuple = split(leftArray)
    leftLeftArray:list = splitLeftArray[0]
    rightLeftArray:list = splitLeftArray[1]

    leftLeftBestPosition:list = divideAndConquerIndex(leftLeftArray)
    rightLeftBestPosition:list = divideAndConquerIndex(rightLeftArray)

    newLeftArray:list = leftArray[leftLeftBestPosition[0]:rightLeftBestPosition[1]+leftHalfwayPoint]
    maxLeftArrayPosition:list = divideAndConquerIndex(newLeftArray)
    #maxLeftArray:list = newArray[maxLeftArrayPosition[0]:maxLeftArrayPosition[1]]
    
    #right side
    rightArray:list = splitArray[1]
    rightArrayLength = len(rightArray)
    rightHalfwayPoint = floor(rightArrayLength/2)

    splitRightArray:tuple = split(rightArray)
    leftRightArray:list = splitRightArray[0]
    rightRightArray:list = splitRightArray[1]

    leftRightBestPosition:list = divideAndConquerIndex(leftRightArray)
    rightRightBestPosition:list = divideAndConquerIndex(rightRightArray)

    newRightArray:list = rightArray[leftRightBestPosition[0]:rightRightBestPosition[1]+rightHalfwayPoint]
    maxRightArrayPosition:list = divideAndConquerIndex(newRightArray)
    #maxRightArray:list = newArray[maxRightArrayPosition[0]:maxRightArrayPosition[1]]
    
    #combine the two
    newArray = array[maxLeftArrayPosition[0] + leftLeftBestPosition[0]:maxRightArrayPosition[1]+halfwayPoint+leftRightBestPosition[0]]
    maxPosition = divideAndConquerIndex(newArray)
    maxArray = newArray[maxPosition[0]:maxPosition[1]]
    endTime = time.perf_counter()

    return (maxArray, endTime-startTime, newArray, newLeftArray, newRightArray)

def main():
    times1 :list = []
    times2:list = []
    times3:list = []

    numRepetitions :int = 20
    for size in range(1, 20):
        arraySize:int = size * 30
    #arraySize:int = 100
        print(f"arraySize: {arraySize}")
        for i in range(numRepetitions):
            newArray :list = createArray(arraySize)
            #print(f"newArray: {newArray}")

            result1:tuple = divideAndConquer1(newArray)
            maxSubArray1 :list = result1[0]
            maxSubArraySum1 = sum(maxSubArray1)
            #print(f"maxSubArray1: {maxSubArray1}")
            #print(f"maxSum1: {maxSubArraySum1}")

            timeTaken1 :float = result1[1]
            times1.append(timeTaken1)

            result2:tuple = divideAndConquer2(newArray)
            maxSubArray2:list = result2[0]
            maxSubArraySum2 = sum(maxSubArray2)
            #print(f"maxSubArray2: {maxSubArray2}")
            #print(f"maxSum2: {maxSubArraySum2}")

            timeTaken2 :float = result2[1]
            times2.append(timeTaken2)

            result3:tuple = divideAndConquer3(newArray)
            maxSubArray3:list = result3[0]
            maxSubArraySum3 = sum(maxSubArray3)
            #print(f"maxSubArray3: {maxSubArray3}")
            #print(f"maxSum3: {maxSubArraySum3}")

            timeTaken3:float = result3[1]
            times3.append(timeTaken3)

            if(maxSubArraySum1 != maxSubArraySum3):
                print("\n discrepancy!")
                print(f"newArray: {newArray}")
                print(f"maxSubArray1: {maxSubArray1}")
                print(f"maxSum1: {maxSubArraySum1}")
                #print(f"maxSubArray2: {maxSubArray2}")
                #print(f"maxSum2: {maxSubArraySum2}")
                print(f"maxSubArray3: {maxSubArray3}")
                print(f"maxSum3: {maxSubArraySum3}")

                newArray = result3[2]
                newLeftArray = result3[3]
                newRightArray = result3[4]
                print(f"newArray: {newArray}")
                print(f"newLeftArray: {newLeftArray}")
                print(f"newRightArray: {newRightArray}")

        averageTime1 :float = sum(times1) / numRepetitions
        print(f"Average Time 1: {averageTime1}")

        averageTime2 :float = sum(times2) / numRepetitions
        print(f"Average Time 2: {averageTime2}")

        averageTime3:float = sum(times3) / numRepetitions
        print(f"Average Time 3: {averageTime3}")

if __name__ == "__main__":
    main()
