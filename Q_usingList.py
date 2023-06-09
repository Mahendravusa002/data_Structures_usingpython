def Enqueue():
    global n
    global front,rear
    if rear==n-1:
        print("already Full...!Queue is OVERFLOW")
        return
    if front==-1 :
        front=0
    ele=int(input("enter element into queue:"))
    rear+=1
    queue.append(ele)
def Dequeue():
    global n
    global front,rear
    if (front==-1 and rear==-1 )or front>rear:
        print("already Empty...!Queue is UNDERFLOW")
        return
    print(queue.pop(front),"element is removed")
    rear-=1
def Qdisplay():
    global front,rear
    if front==-1:
        print("Queue is Empty")
        return
    i=front
    while i<=rear:
        print(queue[i],"\t",end='')
        i+=1
queue=[]
front=-1
rear=-1
n= int(input("enter size of queue:"))
print("OPERTATION OF QUEUE \n 1.Enqueue\n 2.Dequeue\n 3.Qdisplay\n 4.Exit")
while(1):
    ch=int(input("\nenter operation:"))
    if ch==1:
        Enqueue()
    elif ch==2:
        Dequeue()
    elif ch==3:
        Qdisplay()
    elif ch==4:
        break
    else:
        print("OPERTATION OF QUEUE \n 1.Enqueue\n 2.Dequeue\n 3.Qdisplay\n 4.Exit")
        print("enter correct choice")


        
    
    
    
            
    
    
        
