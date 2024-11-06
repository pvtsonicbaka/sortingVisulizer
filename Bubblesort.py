import time

def bubbleSort(data,drawData,timeTick):
    for i in range (len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1]= data[j+1],data[j]
                colorArray = ['yellow' if x == j or x==j+1 else 'Blue' for x in range(len(data)) ]
                drawData(data,colorArray)
                time.sleep(timeTick)
    colorArray = ['green' for _ in range(len(data))]
    drawData(data, colorArray) 
    time.sleep(timeTick) 
    drawData(data, ['lightgreen' for _ in range(len(data))])  
    time.sleep(timeTick) 