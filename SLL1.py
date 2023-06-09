class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            insert_at_begining(data,None)
            return
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=Node(data,None)
    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
    def remove_at_end(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        else:
            itr=self.head
            while(itr.next.next!=None):
                itr=itr.next
            itr.next=None
    def remove_at_begin(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        else:
            self.head=self.head.next
    def get_length(self):
        if self.head is not None:
            c=0
            itr=self.head
            while(itr):
                itr=itr.next
                c+=1
            return c
        else:
            return "ll is empty"
    def remove_at_position(self,index):
        if index<0 or index > self.get_length():
            return "out of index"
        if index==0:
            self.head=self.head.next
            return
        c=0
        itr=self.head
        while(itr):
            if c==index-1:
                itr.next=itr.next.next
            itr=itr.next
            c+=1
    def insert_at_position(self,index,data):
       # if index <0 or index >= self.get_length():
            #return "out of index"
        if index==0:
            self.head=Node(data,self.head)
            return
        c=0
        itr=self.head
        while(itr):
            if c==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            c+=1
        
if __name__ =="__main__":
    ll=LinkedList()
    ll.insert_at_begining('7')
    ll.insert_at_begining('mahiA')
    ll.insert_at_begining('helloB')
    ll.insert_at_end('B')
    ll.insert_at_position(0,34)
    ll.remove_at_end()
    ll.remove_at_begin()
    ll.remove_at_position(0)
    ll.print()
    print(ll.get_length())
    
