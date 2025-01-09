import time
timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray=0,0,0,0

def bubbleSort(data,drawData,timeTick):
    global timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray
    for i in range (len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1]= data[j+1],data[j]
                totalSwaps+=1
                writesToMainArray+=2
                colorArray = ['yellow' if x == j or x==j+1 else 'Blue' for x in range(len(data)) ]
                drawData(data,colorArray)
                time.sleep(timeTick)
                timeOfCompletion+=timeTick
    colorArray = ['green' for _ in range(len(data))]
    drawData(data, colorArray) 
    time.sleep(timeTick) 
    timeOfCompletion+=timeTick
    drawData(data, ['lightgreen' for _ in range(len(data))])  
    time.sleep(timeTick) 
    timeOfCompletion+=timeTick
    return timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray