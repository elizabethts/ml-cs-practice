class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
    

class LinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

  def print_list(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

  def find_element(self, input_data):
    # check the first Node
    cur = self.head
    # if found, return the data
    while cur:
      # repeat until found
      if cur.data == input_data:
        return cur
      else:
        # if not, go to next Node
        cur = cur.next
    # if you get to end of list
    # and next = None, return None
    return False
  
  def append(self, input_data):
    insert_node = Node(input_data)
    
    # if the list is empty
    if self.head == None:
      self.head = insert_node
      self.count += 1
      return 

    # find the cur which points to None
    # iterate through nodes until cur.next is none
    cur = self.head
    while cur.next != None:
      cur = cur.next
    cur.next = insert_node
    self.count += 1
  

  def prepend(self, input_data):
    insert_node = Node(input_data)

    # point the next of the node being inserted to 
    # the current Node
    # head of insert_node needs to point to first node
    insert_node.next = self.head
    self.head = insert_node
    self.count += 1

  def remove(self, input_data):
    # find the prev node of the node that your going to delete
    # point the next of the previous node to the node
    # after the node youre deleting
    # delete the next of the node that you're deleting
    cur = self.head

    if cur.next == None:
      if cur.data == input_data:
          self.head = None
          return True
      else:
        return False
      
    
    while cur.next != None:
      if cur.next.data == input_data:
        cur.next = cur.next.next
        return True
      else:
        return False
     

  def get_size(self):
    return self.count





# Head     First Node      Last Node
# 0 ---> node10 ----> node20 ----> None

# llist.head        second              third 
#          |                |                  | 
#          |                |                  | 
#     +----+------+     +----+------+     +----+------+ 
#     | 1  |  o-------->| 2  |  o-------->|  3 | null | 
#     +----+------+     +----+------+     +----+------+  


# llist = LinkedList()

# # node = Node(10)
# # llist.head = Node(10)
# # llist.head.next = Node(20)
# # llist.head.next.next = Node(30)

# # print(linkedlist.head.data)
# # print(linkedlist.head.next.data)

# llist.print_list()
# # print(llist.find_element(30))
# # llist.prepend(42)
# # llist.print_list()
# llist.append('world')
# llist.prepend('hello')
# llist.append('!')


# # print(llist.get_size())
# # print(f"Count of Linked List: {llist.get_size()}")
# llist.print_list()
# print(llist.get_size())

# llist = LinkedList()
# llist.append('hi')
# llist.print_list()
# llist.remove('hi')  
# llist.print_list()
