class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_first(self,data):
        n=Node(item=data)
        if self.is_empty() is True:
            self.start=n
        else:
            n.next=self.start
            self.start.prev=n
            self.start=n
    def insert_at_last(self,data):
        n=Node(item=data)
        if self.is_empty() is True:
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            n.prev=temp
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(item=data,next=temp.next,prev=temp)
            temp.next.prev=n
            temp.next=n
    def delete_at_first(self):
        if self.start==None:
            pass
        elif self.start.next==None:
            self.start=None
        else:
            self.start.next.prev=None
            self.start= self.start.next
    def delete_at_last(self):
        if self.start==None:
            pass
        elif self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next.prev=None
            temp.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start==None
        else:
            temp = self.start
            if temp.item==data:
                temp.next.prev=None
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        temp.next.prev=temp.next
                    temp=temp.next

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next

    def __iter__(self):
        return DLLItreator(self.start)

class DLLItreator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
    
mylist = DLL()
mylist.insert_at_first(10)
mylist.insert_at_first(20)
mylist.insert_at_first(30)
mylist.insert_at_last(0)
mylist.insert_after(mylist.search(20),15)
mylist.insert_after(mylist.search(10),5)
mylist.insert_after(mylist.search(30),25)
mylist.print_list()
mylist.delete_at_first()
mylist.delete_at_last()
print()
mylist.print_list()
print()
mylist.delete_item(10)
mylist.delete_item(20)
for x in mylist:
    print(x,end=" ")
print()