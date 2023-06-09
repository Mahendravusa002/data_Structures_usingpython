def selection(li):
    for i in range(len(li)):
        min_val=i
        for j in range(i+1,len(li)):
            if(li[j]<li[min_val]):
                min_val=j
        li[i],li[min_val]=li[min_val],li[i]
    print("given list in asending order",li)


#Input entering
lis=input("enter elements to list")
lis=[int(i)for i in lis.split()]
#Function call
selection(lis)


        


