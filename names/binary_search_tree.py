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
import sys
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
    def __len__(self):
        return self.size
        
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if not self.size:
            return None
        
        self.size -= 1
        return self.storage.remove_from_head()


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        
    def __len__(self):
        return self.size
    
    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1
    
    def pop(self):
        if not self.size:
            return
        
        self.size -= 1
        return self.storage.remove_from_head()
        

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        
        if value >= self.value:
            if self.right:
                self.right.insert(value)    
            else:
                self.right = new_node
        
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = new_node
 
    def contains(self, target):
        if self.value == target:
            return True
        
        if target >= self.value:
            return self.right.contains(target) if self.right is not None else False 
        
        return self.left.contains(target) if self.left is not None else False 
                
    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right
            
        return current_node.value
    
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        
        if self.left:
            self.left.for_each(fn)
            
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node = self.value
        
        if self.left:
            self.left.in_order_print(self.left)
            
        print(node)
        
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #make a queue
        #enqueue node
        #as long as the queue is not empty
        ##dequeue from the front of the queue, this is our current node
        ## enqueue the kids of the current node on the queue
        
        my_queue = Queue()
        my_queue.enqueue(node)
        
        while my_queue.size:
            current_node = my_queue.dequeue()  
            print(current_node.value)       
            
            if current_node.left:
                my_queue.enqueue(current_node.left)
           
            if current_node.right:
                my_queue.enqueue(current_node.right)
               
        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        my_stack = Stack()
        my_stack.push(node)
        
        while my_stack.size:
            current_node = my_stack.pop()
            print(current_node.value)
        
            if current_node.left:
                my_stack.push(current_node.left)

            if current_node.right:
                my_stack.push(current_node.right)
              
            
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if(node):
            print(node.value)       
            node.pre_order_dft(node.left)
            node.pre_order_dft(node.right)
            

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if(node):
            node.post_order_dft(node.left)
            node.post_order_dft(node.right)
            print(node.value) 