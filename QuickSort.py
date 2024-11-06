import time 

def partition(data,p,q):
    pivot = data[p]
    i=p
    for j in range(p+1,q):
        if data[j] <=pivot:
            i=i+1
            data[j],data[i] = data[i],data[j]

    data[i],data[p]=data[p],data[i]
    return i

def quicksort(data,p,q):
    if p==q:
        return data
    elif p<q:

        pivotIdx=partition(data,p,q)
        quicksort(data,p,pivotIdx-1)
        quicksort(data,pivotIdx+1,q)
        
        return data
    
data = [1,10,2,1,3,1]

quicksort(data,0,len(data))

print(data)