class Node:
  # creates new Node
  def __init__(self, value):
    self.value = value 
    self.next = None
  

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    # sets head and tail to point at same node to initialize
    self.head = new_node
    self.tail = new_node
    # initializes the length to one node
    self.length = 1

my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""