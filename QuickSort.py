import time 

timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray=0,0,0,0


def partition(data,p,q,drawData,timetick):
    global timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray
    
    pivot = data[p]
    i=p
    drawData(data,colorArray(len(data),p,q,pivot,pivot))
    time.sleep(timetick)
    timeOfCompletion+=timetick



    for j in range(p+1,q):
        if data[j] <=pivot:
            drawData(data,colorArray(len(data),p,q,pivot,j,True))
            time.sleep(timetick)
            timeOfCompletion+=timetick

            i=i+1
            data[j],data[i] = data[i],data[j]
            writesToMainArray+=2
            totalSwaps+=1
            drawData(data,colorArray(len(data),p,q,pivot,j))
            time.sleep(timetick)
            timeOfCompletion+=timetick

    drawData(data,colorArray(len(data),p,q,pivot,q,True))
    time.sleep(timetick)
    timeOfCompletion+=timetick

    data[i],data[p]=data[p],data[i]
    writesToMainArray+=2
    totalSwaps+=1

    return i

def tempQuickSort(data,p,q,drawData,timetick):
    global timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray

    quicksort(data,p,q,drawData,timetick)
    drawData(data,['green' for x in range(len(data))])

    return timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray
    

def quicksort(data,p,q,drawData,timetick):
    if p<q:

        pivotIdx=partition(data,p,q,drawData,timetick)
        quicksort(data,p,pivotIdx,drawData,timetick)
        quicksort(data,pivotIdx+1,q,drawData,timetick)

def colorArray(dataLength,p,q,pivot,currIdx,isSwap=False):
    colorArray=[]
    for i in range(dataLength):
        if i>=p and i <=q:
            colorArray.append("grey")
        else:
            colorArray.append("white")
        if i==q:
            colorArray[i]="orange"
        elif i==pivot:
            colorArray[i]="red"
        elif i==currIdx:
            colorArray[i]="yellow"
        if isSwap:
            if i==pivot or i==currIdx:
                colorArray[i]='green'
    return colorArray



