def insertion(li):
    for i in range(1,len(li)):
        j=i
        while(li[j-1]>li[j] and j>0):
            li[j-1],li[j]=li[j],li[j-1]
            j-=1
    print(li)


li=input("enter elements in list")
li=[int(x) for x in li.split()]
insertion(li)
print("sorted array=",end=' ')
print(li)          

            
            
        

