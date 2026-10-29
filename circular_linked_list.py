class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class Circular_LinkedList:
    def __init__(self):
        self.head=None 
        self.size=0 

    def append(self,data):

        new_node=Node(data)

        if self.head== None:
            self.head=new_node
            new_node.next=self.head

            self.size+=1
            return  
        
        current=self.head 

        while current.next!=self.head:
            current=current.next 
        
        current.next=new_node 
        new_node.next=self.head 
        self.size+=1
    
    def prepend(self,data):
        new_node=Node(data)

        if self.head==None:
            self.head=new_node
            new_node.next=self.head
            self.size+=1
            return 

        current=self.head 

        while current.next!=self.head:
            current=current.next 

        current.next=new_node
        new_node.next=self.head 

        self.head=new_node
        self.size+=1
    
    def insert_at_index(self,index,data):

        if index<0 or index>self.size:
            raise IndexError("INvaliod Index")
        
        if index==0:
            self.prepend(data)
            return 
        
        if index== self.size-1:
            self.append(data)
            return 
        
        new_node=Node(data)

        current=self.head 

        for _ in range(0,index-1):
            current=current.next 
        
        new_node.next=current.next 
        current.next=new_node
        self.size+=1 

    def delete_first(self):
        if self.head==None:
            print("No node exists")
            return 

        if self.head==self.head.next:
            self.head=None
            self.size-=1
            return 

        current=self.head
        deletednodedata=self.head.data
        while current.next!=self.head: 
            current=current.next 

        
        self.head=current.next.next
        current.next=current.next.next 
        self.size-=1
        return deletednodedata

    def delete_last(self):
        if self.head==None:
            print("No node exists")
            return

        if self.head.next==self.head:
            deletednodedata=self.head.data
            self.head=None
            self.size-=1 

            return deletednodedata

        current=self.head 
        while current.next.next!=self.head:
            current=current.next 

        deletenodedata=current.next.data 
        current.next=self.head 
        self.size-=1

        return deletenodedata 

    def delete_at_specificIndex(self,index):
        if index<0 or index>self.size-1:
            print("Invalid Index")
            return

        if index==0:
            return self.delete_first()

        if index==self.size-1:
            return self.delete_last()

        current=self.head 

        for _ in range(index-1):
            current=current.next  
        
        deletednodedata=current.next.data

        current.next=current.next.next 
        self.size-=1

        return deletednodedata

    #some more method I can write are update, deleted by value, reverse the circular list,size, clear,isempty

    def traversal(self):
        if self.head==None:
            print("List is empty")
            return None
        
        current=self.head 

        while True:
            print(current.data,end="->")
            current=current.next

            if current == self.head:
                break
         
      
        

            
