import random 
import time


def isSorted(data):
    for i in range(len(data)-1):
        if data[i]>data[i+1]:
            return False
    return True


def bogosort(data,drawData,timeTick):
    iterations=0
    while not isSorted(data):
        iterations+=1
        i = random.randint(0,len(data)-1)
        j = random.randint(0,len(data)-1)
        #swap
        colorArray = ['Yellow' if x==i or x==j else 'Blue' for x in range(len(data))]
        drawData(data,colorArray)
        data[i],data[j] = data[j],data[i]
        colorArray=['Blue' for x in range(len(data))]
        drawData(data,colorArray)
        time.sleep(timeTick)
    colorArray = ['green' for _ in range(len(data))]
    drawData(data, colorArray) 
    time.sleep(timeTick) 
    drawData(data, ['lightgreen' for _ in range(len(data))])  
    time.sleep(timeTick) 