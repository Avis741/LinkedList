class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None
        self.prev=None 

class Doubly_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0 

    def append(self,data):
        new_node=Node(data)

        if self.head==None:
            self.head=new_node
            self.tail=new_node
            self.size+=1 
            return 
        
        self.tail.next=new_node 
        new_node.prev=self.tail 
        self.tail=new_node
        self.size+=1
         
    
    def prepend(self,data):
        new_node=Node(data)

        if self.head==None:
            self.head=new_node
            self.tail=new_node
            self.size+=1 
            return 
        
        new_node.next=self.head 
        self.head.prev=new_node

        self.head=new_node
        self.size+=1

    def insert_at_index(self,index,data):
        if index<0 or index>self.size:
            raise IndexError("Out of bound index")

        if index==0:
            self.prepend(data)
            return

        if index==self.size:
            self.append(data)
            return

        new_node=Node(data)

        
        if index<self.size//2:
            current=self.head
            for _ in rannge(0,self.size//2):
                current=current.next 
        else:
            current=self.tail 
            for _ in range(self.size-1,index,-1):
                current=current.prev 
        
        new_node.prev=current.prev 
        new_node.next=current

        current.prev.next=new_node
        current.prev=new_node

        self.size+=1
        
    #Deletion of the Node 

    def delete_at_start(self):
        if self.head==None:
            print("no node exits")
            return None

        deleteNodeData=self.head.data

        if self.head==self.tail:
            self.head=None
            self.tail=None 
        else: 
            self.head=self.head.next
            self.head.prev=None

        self.size-=1     
        return deleteNodeData
    
    def delete_at_end(self):
        if self.tail==None:
            print("No node exist")
            return None

        deleteNodeData=self.tail.data 

        if self.head==self.tail:
            self.head=None
            self.tail=None 
        else:
            self.tail=self.tail.prev
            self.tail.next=None 
        
        self.size=-1
        return deleteNodeData
    
    def delete_at_specificIndex(self,index):
        if index<0 or index>self.size:
            raise IndexError("Out of range")

        if index==0:
            return self.delete_at_start()
        if index==self.size-1:
            return self.delete_at_end()

        current=self.head 

        for _ in range(index):
            current=current.next 
        
        deleteNodeData=current.data

        current.prev.next=current.next
        current.next.prev=current.prev 

        self.size-=1
        return deleteNodeData
    
    def reverse(self):
        if self.head is None:
            print("Empty List")
            return

        self.tail = self.head
        current = self.head
        prevNode = None

        while current:
            nextNode = current.next

            current.next = current.prev
            current.prev = nextNode

            prevNode = current
            current = nextNode

        self.head = prevNode
        



         

    
    def traverse_forward(self):
        current=self.head 

        while current:
            print(current.data,end="<->")
            current=current.next 
    
    def traverse_backword(self):
        current=self.tail

        while current:
            print(current.data,end="<->")
            current=current.prev

        