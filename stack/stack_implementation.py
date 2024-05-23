class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

class Stack:
  #Using a dummy node to handle edge cases
  def __init__(self):
    self.head = Node("head")
    self.size = 0

  #string representation of stack
  def __str__(self):
    curr = self.head.next
    output =""
    while curr:
      output = str(curr.val)+ "->"
      curr = curr.next
    return output[:-2] #to avoid last null and -> 
    
  
  def size(self):
    return self.size

  def isEmpty(self):
    return self.size == 0

  def peek(self):
    if self.isEmpty:
      raise Exception("Stack is Empty")
    return self.head.next.val

  def push(self):
    node = Node(self)
    #moving pointers
    node.next = self.head # making the pointers of self as node after new node 
    self.head = node # makin the new node as head
    self.size+=1

  def pop(self):
    if self.isEmpty():
            raise Exception("Popping from an empty stack")
    remove = self.head.next #storing the value to return it later
    self.head.next = self.head.next.next
    self.size -= 1
    return remove.val 
