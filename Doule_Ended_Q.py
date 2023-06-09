class DEQueue:
    def __init__(self):
        self.queue=[]
        self.count=0
    '''def __repr__(self):
        deq=''
        if self.count==0:
            deq ="Double ended Q IS EMPTY"
        else:
            deq+="Double ended Q:\n"+self.DEQueue__repr__()
        print(deq)'''
    def display(self):
        if self.count==0:
            print( "DEQ is Empty")
            return
        print(self.queue)
    def insert_start(self,data):
        if self.count==0:
            self.queue=[data,]
            self.count=1
            return
        self.queue.insert(0,data)
        self.count+=1
        return
    def insert_end(self,data):
        if self.count==0:
            self.queue=[data,]
            self.count=1
            return
        self.queue.append(data)
        self.count+=1
        return
    def remove_start(self):
        if self.count==0:
            raise ValueError("Invalid operation")
        x=self.queue.pop(0)
        self.count-=1
        return x
    def remove_end(self):
        if self.count==0:
            raise ValueError("Inavlid operation")
        x=self.queue.pop()
        self.count-=1
        return x
DQ=DEQueue()
print("OPERATION OF DoubleEndedQ\n1.insert at start  2.insert at end"
      "  3.remove at start\n4.remove at end   5.display\t   6.Exit")
while(1):
    ch=int(input("Enter Operation:"))
    if ch==1 or ch==2:
        k=int(input("enter element:"))
        if ch==1:
            DQ.insert_start(k)
        else:
            DQ.insert_end(k)
    elif ch==3 or ch==4:
        if ch==3:
            print(DQ.remove_start(),"removed")
        else:
           print( DQ.remove_end(),"removed")
    elif ch==5:
        DQ.display()
    elif ch==6:
        print("EXITING...")
        break
    else:
        print("enter COrrect operation!")
        print("OPERATION OF DoubleEndedQ\n1.insert at start  2.insert at end"
      "  3.remove at start\n4.remove at end   5.display\t   6.Exit")
    
        

            
        
