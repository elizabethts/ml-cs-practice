"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):

        if not isinstance(value, ListNode):
            insert_node = ListNode(value)
        else:
            insert_node = value

        print('node created')

        if self.head == None and self.tail == None:
            self.head = insert_node
            self.tail = insert_node
            print('new node inserted in empty list')

        else:
            # Point insert_node's next to current node
            insert_node.next = self.head
            # Point the prev of current node to insert_node
            self.head.prev = insert_node
            # Head of insert_node needs to point to first node
            self.head = insert_node
            self.head.prev = None
            print('new node inserted')

        # increment length
        self.length += 1




    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # if node is in both head/tail (dll of length 1, or head==tail)
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # if node is the head
        elif self.head is node:
            # make the next pointer of the current node the head
            self.head = node.next
            # delete the node
            node.delete()
        # if node is the tail
        elif self.tail is node:
            # make the previous node the tail
            self.tail = node.prev
            # delete the node
            node.delete()
        # if node is in middle
        else:
            node.delete()
        # decrement length
        self.length -= 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""


    def remove_from_head(self):

        # check if list is empty
        if self.head:
            print('hi im here self.head')
            print(self.head.value, self.tail.value)
            value = self.head.value
            self.delete(self.head)
            print(value)
            return value


    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):

        if not isinstance(value, ListNode):
            insert_node = ListNode(value)
        else:
            insert_node = value

        # check if list is empty
        # if empty, make the new value both head and tail
        if self.head == None and self.tail == None:
            self.head = insert_node
            self.tail = insert_node

        # if list already has nodes
        # save current tail
        # make the new value the tail
        # point to prev pointer of the tail to the saved var
        # make the next pointer of the old tail the new node

        else:
            old_tail = self.tail
            self.tail = insert_node
            self.tail.prev = old_tail
            old_tail.next = self.tail
            self.tail.next = None

        # increment length
        self.length += 1


    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # check if list is empty
        # if empty return false
        if self.head == None and self.tail == None:
            return False

        # if list is not empty
        # save the next pointer of the tail's prev node
        # set the next pointer of the tail's prev node = self.tail
        # point the prev pointer of the tail to saved var
        # set the next pointer of tail = None
        # return value of removed node
        # decrement length
        if self.tail:
            value = self.tail.value
            cur_prev = self.tail.prev
            print('printing cur_prev', cur_prev)

            self.tail.prev = None
            self.tail = cur_prev

            # self.tail.prev = None
            # if cur_prev != None:
            #     self.tail.next = None


            if cur_prev == None:
                print('update head to none')

                self.head = None



            # decrement length
            self.length -= 1

            return value


    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):

        # delete the node
        # use add to head to insert in front
        self.delete(node)
        print('node deleted')

        self.add_to_head(node)
        print('node added to front')



    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):

        # delete the node
        # use add to tail to insert at end
        self.delete(node)
        print('node deleted')

        self.add_to_tail(node)
        print('node added to tail')
        print('tail value:', self.tail.value)


    """Returns the highest value currently in the list"""

    def get_max(self):

        # cur_max = 0
        # iterate through each node
        # while node.next != None
        # get the value
        # set max to value if value is larger

        cur = self.head
        cur_max = self.head.value

        while cur != None:
            value = cur.value
            print('value', value)

            if value > cur_max:
                cur_max = value

            cur = cur.next

        return cur_max



