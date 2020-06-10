"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
    -   You have to keep track of the size of the list becuase a singularly linked list doesn't have reference to every element.
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size = self.size + 1

#     def pop(self):
#         if self.size == 0: return None
#         self.size = self.size - 1
#         return self.storage.pop(self.size - 1)

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        node = Node(value)
        self.storage.add_to_tail(node)
        self.size = self.size + 1

    def pop(self):
        if self.size == 0: return None
        self.size = self.size - 1
        return self.storage.remove_tail()

# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------

class Node:

    def __init__(self, value, next_node=None):
        # Initialize the node with a value and next_node property. `next_node` defaults to none.
        self.value = value
        self.next = next_node

    def get_value(self):
        # Return the current value being held inside the node.
        return self.value

    def set_value(self, value):
        # Set the value of the current node to hold `value` property.
        self.value = value

    def get_next(self):
        # Returns the next node in sequence or None if there is not one.
        return self.next
    
    def set_next(self, node):
        # Sets the next node in sequence.
        self.next = node

class LinkedList:
    def __init__(self):
        # Initialize the LinkedList with an empty list. Empty list achieved by defaulting head and tail to None.
        self.head = None
        self.tail = None

    '''
    Appends 'data' (typeof Node) property to the end of the LinkedList sequence.
    Runtime complexity is O(1) becuase the operation does not depend on the size of the linked list.
    '''
    def add_to_tail(self, data):

        # Initalize a new node with the data passed.
        new_node = Node(data)

        # Check to see if head and tail are both 'None'.. If so, 'new_node' becomes both head and tail because it will be the only item in the list.
        if not self.head and not self.tail:
            # List is empty, set both head and tail to 'new_node'.
            self.head = new_node
            self.tail = new_node
        else:
            # List is not empty.
            
            # 1. Set the next property of the current tail to the 'new_node'.
            self.tail.set_next(new_node)

            # 2. Set self.tail to 'new_node'.
            self.tail = new_node

    '''
    Remove the current 'self.tail' Node and return it's value.
    O(n) is the runtime complexity because we will have to loop through and get the second to last node.
    '''
    def remove_tail(self):

        # Check to see if the list is empty. If so, return 'None'.
        if self.tail is None:
            return None

        # Retrieve the data on current self.tail.
        data = self.tail.get_value()

        # If the head and tail are the same, that means there is only one item in the array.
        # Therefore, set both head and tail to None to empty the list.
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            # In order to update `self.tail` to point to the
            # the Node before the tail, we need to traverse
            # the whole linked list starting from the head,
            # because we cannot move backwards from any one.
            current = self.head

            # Traverse until we get to the Node right before tail.
            while current.get_next() != self.tail:
                current = current.get_next()

            # 'current' is now pointing at the Node right
            # before the tail Node.
            self.tail = None
            self.tail = current
        
        return data.get_value()

    '''
    Removes the Node that 'self.head' is referring to and returns the Node's data.
    Runtime complexity would be O(1) because there are not loops, and only setting values.
    '''
    def remove_head(self):
        
        # Check to see if 'self.head' is None (this means the array is empty).
        if self.head is None:
            return None

        data = self.head.get_value()

        # Check to see if head and tail is the same Node, if so remove them both.
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            # There is more than one node in the list.
            # To delete the head Node, we only have to set 'self.head' to the second node instance.
            self.head = self.head.get_next()
        
        return data

    '''
    Traverse the linked list and return a boolean indicating whether the
    specified 'data' is in the linked list.

    Runtime complexity is O(n) because we have to loop each element at least once.
    '''
    def contains(self, data):
        # Check to see if the list is empty, this is indicated by an empty head.
        if not self.head:
            return False

        # Get a reference to the first Node in the linked list.
        # We update what this Node points to as we traverse the linked list.
        current = self.head

        # Traverse the linked list so long as current is referring to a Node.
        while current is not None:
            # Check if the Node that 'current' is pointing at is holding the data we are looking for.

            if current.get_value() == data:
                return True
            
            # Data was not in the current node, move on to the next node and keep checking.
            current = current.get_next()
        
        # At this point we have loops through entire list and nothing was found, return False.
        return False

    '''
    Traverse the linked list, fetching the max value in the linked list.

    Runtime is O(n) because we are looping the entire list atleast once.
    '''
    def get_max(self):
        # Check to make sure the list is not empty.
        if self.head is None:
            return None

        max_so_far = self.head.get_value()

        current = self.head.get_next()

        while current is not None:
            if current.get_value() > max_so_far:
                max_so_far = current.get_value()
            current = current.get_next()
        
        return max_so_far