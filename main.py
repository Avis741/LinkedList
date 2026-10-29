from linked_list import Linked_List
from doubly_linked_list import Doubly_linked_list
from circular_linked_list import Circular_LinkedList

#obj=Linked_List()
#obj.append(10)
#obj.append(20)
#obj.append(30)

#obj.traversal(obj.head)

#obj=Doubly_linked_list()
#obj.append(10)
#obj.append(20)
#obj.append(30)
#obj.append(40)
#obj.prepend(5)
#obj.insert_at_index(0,5)
#obj.traverse_forward()
#print()
#obj.traverse_forward()
#print()
#print(obj.delete_at_specificIndex(1))
#print(obj.head)
#bj.traverse_forward()
#print(obj.size)
#obj.traverse_backword()
#print(obj.size)

#################Circular Linked List

'''
obj=Circular_LinkedList()
obj.append(10)
obj.append(20)
obj.append(30)


obj.traversal()
#obj.insert_at_index(3,35)
print()
obj.delete_at_specificIndex(2)
obj.traversal()
'''
obj=Linked_List()
obj.append(1)
obj.append(2)
obj.append(1)
obj.append(3)
obj.append(4)
obj.append(1)

obj.traversal()
print(obj.palindrome())



