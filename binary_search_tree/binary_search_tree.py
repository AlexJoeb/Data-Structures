import sys

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # 1. Compare the value to the root's value to determine which direction to go.
        if value < self.value:
            # -- Go Left --
            # Check if there is another node on the left.
            if self.left:
                # -- There is a node on the left. --
                # Run this function, but on the node that is one to the left.
                self.left.insert(value)
            else:
                # -- There is not a node on the left, and we can place the value there. --
                self.left = BSTNode(value)
        else:
            # -- Value is >= to root's value.. Go right.
            # Check to see if there is a node to the right.
            if self.right:
                # -- There is a node to the right. --
                # Run this function, but on the node that is one to the right.
                self.right.insert(value)
            else:
                # -- There is not a node to the right. --
                # Go ahead and place the value on the right.
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check the current node is equal to target.
        if self.value == target: return True
        else:
            # Current value is not equal to target.

            if target < self.value:
                # Target is less than root's value.
                # Go left.

                # Check to see if there is a node on the left.
                if not self.left:
                    # There is not a node on the left.
                    return False
                else:
                    # There is a node to the left.
                    # Use recursion to run this function on the next node.
                    return self.left.contains(target)
            else:
                # Target is greater than root's value.
                # Go right.
                
                # Check to see if there is a node on the right.
                if not self.right:
                    # There is not a node on the right.
                    return False
                else:
                    # There is a node to the left.
                    # Use recursion to run this function on the next node.
                    return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        current = self;
        while(current.right != None):
            current = current.right
        return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        
        if(self.left):
            self.left.for_each(fn)
        
        if(self.right):
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(f'{node.value}')
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if not node:
            return None
        else:
            Q = []
            Q.append(node)
            final = ''
            while(Q):
                front = Q[0]
                if front.left:
                    Q.append(front.left)
                if front.right:
                    Q.append(front.right)

                print(front.value)
                Q.pop(0)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal 
    def dft_print(self, node):
        if node:
            self.pre_order_dft(node.left)
            print(node.value)
            self.pre_order_dft(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)