#soon
from time import *


def insertionSort(data,drawData,tick):
    colorArray = ['white' for x in range(len(data))]
    drawData(data,colorArray)
    sleep(tick)
    for i in range(1,len(data)):  
        j=i-1
        key=data[i]
        colorArray[i] = 'blue'
        drawData(data,colorArray)
        sleep(tick)

        while  j>=0 and data[j]>key:
            colorArray[j] ='red'
            colorArray[j+1]='orange'
            drawData(data,colorArray)

            data[j+1]=data[j]
            colorArray[j]='orange'
            j-=1
            sleep(tick)
        data[j+1]=key
        sleep(tick)


    
    colorArray=['green' for x in range(len(data))]
    drawData(data,colorArray)

    return data

    

data=[2,1,10,99,23,56,33,5,6]
# print(insertionSort(data))
            
            
