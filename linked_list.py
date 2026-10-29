class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 

class Linked_List:
    def __init__(self):
        self.head=None
        self.size=0 
    

    def isempty(self):

        return self.head is None
        if self.head:
            return False
        else:
            return True 
    
    def length(self):
        return self.size

    def prepend(self,data):
        new_node=Node(data)

        new_node.next=self.head 
        self.head= new_node
        self.size+=1


    #insertion at the end
    def append(self,data):
        new_node=Node(data)
        
        if self.head is None:
            self.head=new_node
            self.size+=1
            return 
        
        current=self.head 

        while current.next is not None:
            current=current.next

        current.next=new_node
        self.size+=1

    #At any index
    def insert(self,index,data):
        if index<0 or index>self.size:
            raise IndexError("Invalid Index")
        
        if index==0:
            self.prepend(data)
            return
        
        current=self.head

        for _ in range(index-1):
            if current is None:
                raise IndexError("Invalid Index")
            current=current.next

        if current is None:
            raise IndexError("Invalid Index") 

        new_node=Node(data)
        new_node.next=current.next
        current.next=new_node
        self.size+=1

    #delete the first index
    def delete_first(self):
        if self.head is None:
            return None

        deleted_node_data=self.head.data 
        self.head=self.head.next
        self.size-=1
        return deleted_node_data 

    def delete_last(self):

        if self.head is None:
            return None

        if self.head.next is None:
            return self.delete_first

        current=self.head 

        while current.next.next:
            current=current.next

        deleted_node_data=current.next.data 
        current.next=None
        self.size-=1 
        return deleted_node_data


    #deleteBy value first occurance
    def delete_by_value(self,value):
        if self.head is None:
            return False 

        if self.head.data==value:
            return self.delete_first() 
        
        current=self.head 
        deleted_node_data=None
        while current.next:
            if current.next.data==value:
                current.next=current.next.next
                self.size-=1
                return True
            current=current.next

    def delete_by_index(self,index):
        if self.head is None:
            return False

        if index<0 or index>=self.size:
            raise IndexError("invalid index")

        if index==0:
            return self.delete_first()

        current=self.head
        cnt=0 
        while current.next:
            cnt+=1
            if cnt==index:
                current.next=current.next.next
                self.size-=1
                return True
            current=current.next

    # 10. Search for a value
    # Returns its first index, or -1 if not found
    def search(self, value):
        current=self.head

        index=0
        while current: 
            if current.data==value:
                return index 
            current=current.next
            index+=1
        
        return -1
    
    #get the value at that index, we can use the same in delete by index, here reutrn the data
    def get(self,index):
        if index<0 or index>=self.size:
            raise IndexError("Invalid Index")
     

        current=self.head

        for _ in range(index):
            current=current.next

        return current.data 
        

    def update(self,index,new_data):
        if index<0 or index>=self.size:
            raise IndexError("Invalid Index")
     

        current=self.head

        for _ in range(index):
            current=current.next
        
        old_data=current.data 
        current.data=new_data

        return old_data
    
    def clear(self):
        self.head=None 
        self.size=0 
    
    def reverse(self): 
        
        current=self.head
        prev=None 

        while current:
            nextNode=current.next
            
            current.next=prev
            prev=current
            current=nextNode

        self.head=prev    

    def find_middle(self):
        if self.head==None:
            return None

        if self.size<2:
            return self.head 
        
        current=self.head 
        
        cnt=0
        while current:
            cnt+=1
            current=current.next 
        
        index=cnt//2 
        current=self.head 
        for _ in range(0,index):
            current=current.next 

        return current.data
            
    def traversal(self):

        current=self.head

        while current:
            print(current.data,end="->")
            current=current.next
    
    def remove_N_from_end(self,n):
        if n<0 or n>self.size:
            print("Wrong Index")
            return 

        count=0
        current=self.head 

        while current:
            count+=1 
            current=current.next 
        
        index=count-n 

        res= self.delete_by_index(index)
        return res 
             
    def palindrome(self):

        current=self.head 
        lst=[]
        while current:
            lst.append(current.data)
            current=current.next 

        current=self.head 
        for x in range(len(lst)-1,-1,-1):
            if lst[x]!=current.data:
                return False 
            current=current.next 
        return True     




