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
        # Get a reference to the node we want to insert after.
        current_next = self.next
        # Set the 'self.next' of target node to the new node (with value) that we are inserting.
        self.next = ListNode(value, self, current_next)
        # Make sure that if current next is not None, that we link it's prev to the node being inserted.
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
        # Before deleting self, we must link the node's next and prev together to maintain the chain.
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
        node = ListNode(value, None, self.head)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.head.prev = node
            self.head = node
            self.length += 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if not self.head and not self.tail:
            # List is empty
            return None
        else:
            data = self.head.value
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                data = self.head.value
                self.head = self.head.next
                self.head.prev = None

            self.length -= 1
            return data

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        node = ListNode(value, self.tail, None)
        if not self.head and not self.tail:
            # List is empty.
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None
        elif self.head is self.tail:
            data = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return data
        else:
            data = self.tail.value
            
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1

            return data

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if not self.head and not self.tail:
            # Both head and tail are None
            return None
        elif self.head is self.tail:
            return None
        else:
            # Bind the two node before and after the moving node together.
            if node.next and node.prev:
                node.prev.next = node.next
                node.next.prev = node.prev
            elif not node.next and node.prev:
                node.prev.next = None
            elif node.next and not node.prev:
                return None
            
            self.head.prev = node
            node.prev = None
            node.next = self.head
            self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # If list is empty, return nothing.
        if not self.head and not self.tail:
            return None
        
        # If node is self.tail, then it already at the end.
        elif self.tail is node:
            return None

        # There are only two elements in the sequence.
        elif self.head is node and self.head.next is self.tail:
            self.head = self.tail
            self.tail = node
            self.head.prev = None
            self.head.next = self.tail
            self.tail.next = None
            self.tail.prev = self.head

        # There are more than two element in the sequence and node is not head or tail.
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            self.tail.next = node
            node.prev = self.tail

            self.tail = node        


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:
            return None # List is empty
        elif self.head is self.tail:
            # There was only one item in the list to delete, assume it was the node
            self.head = None
            self.tail = None
        else:
            if self.head is node:
                # Handles if node is head.
                self.head = self.head.next
                self.head.prev = None
            elif self.tail is node:
                # Handles if node is tail.
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                # Node is somewhere in the middle.
                node.prev.next = node.next
                node.next.prev = node.prev

        
        
        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current = self.head
        max_value = self.head.value
        while current != None:
            if current.value > max_value:
                max_value = current.value
            
            current = current.next
        return max_value