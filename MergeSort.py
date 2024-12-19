import time

def merge_sort(data,drawData,timetick):
    mergeAlgo(data,0,len(data)-1,drawData,timetick)
def mergeAlgo(data,left,right,drawData,timetick):
    if left<right:
        middle=(left+right)//2
        mergeAlgo(data,left,middle,drawData,timetick)
        mergeAlgo(data,middle+1,right,drawData,timetick)
        merge(data,left,middle,right,drawData,timetick)


def merge(data,left,middle,right,drawData,timetick):

    drawData(data,colorArray(len(data),left,middle,right))
    time.sleep(timetick)

    leftPart=data[left:middle+1]
    rightPart=data[middle+1:right+1]

    leftIdx=rightIdx=0
 
    for dataIdx in range(left,right+1):
        if leftIdx<len(leftPart) and rightIdx <len(rightPart):
            if leftPart[leftIdx] <=rightPart[rightIdx]:
                data[dataIdx]=leftPart[leftIdx]
                leftIdx+=1
            else:
                data[dataIdx] =rightPart[rightIdx]
                rightIdx+=1
        elif leftIdx<len(leftPart):
            data[dataIdx]=leftPart[leftIdx]
            leftIdx+=1
        else:
            data[dataIdx]=rightPart[rightIdx]
            rightIdx+=1
    drawData(data,["green" if x>=left and x<=right else "white" for x in range((len(data)))])
    time.sleep(timetick)
def colorArray(length,left,middle,right):
    colorArray=[]
    for i in range(length):
        if i>=left and i<=right:
            if i>=left and i<=middle:
                colorArray.append("yellow")
            else:
                colorArray.append("blue")
        else:
            colorArray.append("white")
    return colorArray
