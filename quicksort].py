#For asending order
def quicksort(arr,left,right):
    if left<right:
        p=partition(arr,left,right)
        quicksort(arr,left,p-1)
        quicksort(arr,p+1,right)
def partition(arr,left,right):
    pivot=arr[right]
    i=left
    j=right-1
    while i<j:
        while i<right and arr[i]<=pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i
li=input("enter list of items")
li=[int(i) for i in li.split()]
quicksort(li,0,len(li)-1)
print("soreted array",end='')
print(li)


#For desinding order
'''while i<j:
        while i<right and arr[i]>=pivot:
            i+=1
        while j>left and arr[j]<=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]<pivot:
        arr[i],arr[right]=arr[right],arr[i]'''
        
