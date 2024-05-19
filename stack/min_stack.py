class MinStack(object):

    def __init__(self):
      self.top_node = None
      self.stack = []

    def __init__(self, min, val):
      self.val = val
      self.min =min
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
       if self.top_node is None or val < self.top_node.min:
            node = self.Node(val=val, min=val)
       else:
            node = self.Node(val=val, min=self.top_node.min)
       self.top_node = node
       self.stack.append(node)

        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop() #removing the top node
        if self.stack:
            self.top_node = self.stack[-1] #changing the value of top node
        else:
            self.top_node = None #changing the value of top node to none if the stack is empty

    def top(self):
        """
        :rtype: int
        """
        if self.top_node is None:
            return None
        else:
            return self.top_node.val

    def getMin(self):
        """
        :rtype: int
        """
          def getMin(self):
        if self.top_node is None:
            return None
        else:
            return self.top_node.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
