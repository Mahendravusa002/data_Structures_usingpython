class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Queue:
    def __init__(self):
        self.head=None
    def enqueue(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=node
    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return
        self.head=self.head.next
    def Qdisplay(self):
        if self.head is None:
            print("Queue is empty")
            return
        itr=self.head
        Q=''
        while(itr):
            Q+=str(itr.data)+" "
            itr=itr.next
        print(Q)
l=Queue()
print("OPERTATION OF QUEUE \n 1.Enqueue\n 2.Dequeue\n 3.Qdisplay\n 4.Exit")
while(True):
    ch=int(input("\nenter operation:"))
    if ch==1:
        k=int(input("enter element"))
        l.enqueue(k)
    elif ch==2:
        l.dequeue()
    elif ch==3:
        l.Qdisplay()
    elif ch==4:
        print("EXITING")
        break
    else:
        print("OPERTATION OF QUEUE \n 1.Enqueue\n 2.Dequeue\n 3.Qdisplay\n 4.Exit")
        print("enter correct choice")
            
        
        
            
