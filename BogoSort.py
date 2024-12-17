import random 
import time


def isSorted(data):
    for i in range(len(data)-1):
        if data[i]>data[i+1]:
            return False
    return True


timeOfCompletion=0
totalSwaps=0
writesToAuxilaryArray=0
writesToMainArray=0


def bogosort(data,drawData,timeTick):

    global timeOfCompletion 
    global totalSwaps
    global writesToAuxilaryArray
    global writesToMainArray


    while not isSorted(data):
        i = random.randint(0,len(data)-1)
        j = random.randint(0,len(data)-1)
        #swap
        colorArray = ['Yellow' if x ==i or x==j else 'Blue' for x in range(len(data))]
        drawData(data,colorArray)
        time.sleep(timeTick)

        data[i],data[j] = data[j],data[i]
        totalSwaps+=1
        writesToMainArray+=1
        colorArray=['Blue' for x in range(len(data))]
        drawData(data,colorArray)
        time.sleep(timeTick)
        
        timeOfCompletion+=1
    colorArray = ['green' for _ in range(len(data))]
    drawData(data, colorArray) 
    time.sleep(timeTick) 
    timeOfCompletion+=1
    drawData(data, ['lightgreen' for _ in range(len(data))])  
    time.sleep(timeTick) 

    return timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray
    