#soon
from time import *


timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray=0,0,0,0

def insertionSort(data,drawData,tick):
    global timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray

    colorArray = ['white' for x in range(len(data))]
    drawData(data,colorArray)
    sleep(tick)
    timeOfCompletion+=tick
    for i in range(1,len(data)):  
        j=i-1
        key=data[i]
        colorArray[i] = 'blue'
        drawData(data,colorArray)
        sleep(tick)
        timeOfCompletion+=tick

        while  j>=0 and data[j]>key:
            colorArray[j] ='red'
            colorArray[j+1]='orange'
            drawData(data,colorArray)

            data[j+1]=data[j]
            writesToMainArray+=2
            totalSwaps+=1
            colorArray[j]='orange'
            j-=1
            sleep(tick)
            timeOfCompletion+=tick
        data[j+1]=key
        writesToMainArray+=1
        sleep(tick)
        timeOfCompletion+=tick


    
    colorArray=['green' for x in range(len(data))]
    drawData(data,colorArray)

    return timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray

    

data=[2,1,10,99,23,56,33,5,6]
# print(insertionSort(data))
            
            
