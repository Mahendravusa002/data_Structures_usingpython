
def linearHashing(li,m):
    global d
    for i in li:
        r=i%m
        if d[r]==0:
            d[r]=i
        else:
            j=0
            while(d[r]!=0):
                j+=1
                r=(i+j)%m
            d[r]=(i)
def display():
    global d
    for i,j in d.items():
        if j!=0:
            print(i,"-->",j)
        else:
            print(i,"-->")
            



l=input("enter list of numbers:")
l=[int(i) for i in l.split()]
m=int(input("enter m value:"))
d={i:0 for i in range(m)}
linearHashing(l,m)
print("HASH TABLE")
display()

    
            
