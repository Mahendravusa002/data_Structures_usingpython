class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class DLL:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,data):
        node=Node(data)
        if self.head is not None:
            node.next=self.head
            self.head.prev=node
        self.head=node
    def printDll(self):
        if self.head is None:
            return"DLL is EMPTY"
        ll=''
        itr=self.head
        while(itr):
            ll+=str(itr.data)+' <====> '
            itr=itr.next
        print(ll)
    def remove_at_begin(self):
        if self.head is None:
            return "DLL is EMPTY"   
        self.head=self.head.next
        self.prev=None
    def Dlllength(self):
        c=0
        if self.head is None:
            return 'DLL is EMPTY'
        itr=self.head
        while itr:
            c+=1
            itr=itr.next
        return c
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_begin(self,data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        node=Node(data)
        itr.next=node
        node.prev=itr
    def remove_at_end(self):
        if self.head is None:
            return "DLL is EMPTY"
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None
    def insert_at_position(self,index,data):
        if index <0 or index >=self.Dlllength():
            print("OUT OF INDEX ")
        c=0
        itr=self.head
        while(itr.next):
            if c==index-1:
                node=Node(data)
                node.prev=itr
                node.next=itr.next
                itr.next=node
                return
            itr=itr.next
            c+=1
    def remove_at_position(self,index):
        if index <0 or index>self.Dlllength():
            return "OUT_OF_INDEX "
        if index ==0:
            self.remove_at_begin()
            return
        c=0
        itr=self.head
        while(itr.next):
            if c==index-1:
                temp=itr.next
                itr.next.next.prev=itr
                temp.prev=None
                itr.next=itr.next.next
                temp.next=None
                return
            itr=itr.next
            c+=1
            
l=DLL()
l.insert_at_begin(3)
l.insert_at_begin(39)
l.printDll()
#l.remove_at_begin()
print("LENGTH IS ",l.Dlllength())
l.insert_at_end(32222)
#l.remove_at_end()
l.insert_at_position(1,564)
#l.insert_at_position(5,564)
l.printDll()
l.remove_at_position(0)
l.printDll()
