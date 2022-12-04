class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      # TODO complete Node initialization 
      self.leftchild = None
      self.rightchild = None
      self.parent = None
      self.__height = 1 


    def getheight(self):
      return self.__height
    
    
    def setheight(self):
      left = right = 0
      if(self.leftchild is None):
        left = 0
      else:
        left = self.leftchild.getheight()
      if(self.rightchild is None):
        right = 0
      else:
        right = self.rightchild.getheight()
      
      if(left < right):
        self.__height = right + 1
      else:
        self.__height = left + 1

    
    def get_balance(self):
      if self.leftchild is None:
        leftheight = 0
      else:
        leftheight = self.leftchild.getheight()
      if self.rightchild is None:
        rightheight = 0
      else:
        rightheight = self.rightchild.getheight()
      balance = rightheight - leftheight
      return balance
    
    
    def rotate_right(self):
      parent = self.parent
      temp = self.leftchild
      temp.parent = parent
      if parent.leftchild == self:
        parent.leftchild = temp
      else:
        parent.rightchild = temp
      
      righttemp = temp.rightchild
      if righttemp is not None:
        righttemp.parent = self
      temp.rightchild = self
      self.parent = temp
      self.leftchild = righttemp
      self.setheight()
      temp.setheight()


    def rotate_left(self):
      parent = self.parent
      temp = self.rightchild
      temp.parent = parent
      if parent.leftchild == self:
        parent.leftchild = temp
      else:
        parent.rightchild = temp
      
      lefttemp = temp.leftchild
      if lefttemp is not None:
        lefttemp.parent = self
      temp.leftchild = self
      self.parent = temp
      self.rightchild = lefttemp
      self.setheight()
      temp.setheight()
      
        
  def __init__(self):
    self.__root = self.__BST_Node(None)
    # TODO complete initialization
    self.__size = 0
    self.height = 0


  def __set_height_of_root(self, val):
    self.height = val
    
    
  def set_root(self,value):
    self.__root.leftchild = self.__BST_Node(value)
    self.__root.rightchild = self.__root.leftchild
    self.__root.leftchild.parent = self.__root
    
    
  def get_root(self):
    return self.__root.leftchild
  
  
  def __balance(t):
    balance = t.get_balance()
    if abs(balance) < 2:
      return t
    else:
      # t is left heavy by 2:
      if balance == -2:
        child = t.leftchild
        # t's leftchild is left-heavy by 1 or 0
        if(child.get_balance() <= 0): 
          t.rotate_right()
          
          """"
          Because t is rotate, we need to return its parent as the new root for the remove method
          in order to get t's orginal parent link to the correct node.
          """
          return t.parent
        # t's leftchild is right-heavy by 1
        else:
          t.leftchild.rotate_left()
          t.rotate_right()
          return t.parent
      # t.balance = 2    
      elif balance == 2:
        child = t.rightchild
        if(child.get_balance() >= 0):
          t.rotate_left()
          return t.parent
        else:
          t.rightchild.rotate_right()
          t.rotate_left()
          return t.parent


  def __recursive_insert(self,value,root):
    if (value == root.value):
      raise ValueError
    else:
      if(value < root.value and root.leftchild is None):
        root.leftchild = self.__BST_Node(value)
        root.leftchild.parent = root
        root.setheight()
        Binary_Search_Tree.__balance(root)
        root.setheight()

      elif(value < root.value and root.leftchild is not None):
        self.__recursive_insert(value,root.leftchild)
        root.setheight()
        Binary_Search_Tree.__balance(root)
        root.setheight()

      elif(value > root.value and root.rightchild is None):
        root.rightchild = self.__BST_Node(value)
        root.rightchild.parent = root
        root.setheight()
        Binary_Search_Tree.__balance(root)
        root.setheight()

      else:
        self.__recursive_insert(value,root.rightchild)
        root.setheight()
        Binary_Search_Tree.__balance(root)
        root.setheight()

  
  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    # try:
    if(self.get_root() is None):
      self.set_root(value)
      self.__set_height_of_root(1)
    else:
      self.__recursive_insert(value, self.get_root()) 
      self.__set_height_of_root(self.get_root().getheight())

  
  def __recursive_remove(self, root, val):
    # Doesn't find the value we want
    if root is None:
      raise ValueError
    
    # intended value < current.value, go left
    if val < root.value:
      root.leftchild = self.__recursive_remove(root.leftchild, val)
      root.setheight()
      if root.leftchild is not None:
        root.leftchild.parent = root

    # intended value > current.value, go right
    elif val > root.value:
      root.rightchild = self.__recursive_remove(root.rightchild,val)

      root.setheight()
      if root.rightchild is not None:
        root.rightchild.parent = root
    
    # find the value we want to remove, check how to remove it.
    else:
      if root.rightchild is None:
        return root.leftchild
      if root.leftchild is None:
        return root.rightchild
      # both left and right has subtrees  
      else:
        temp = root.rightchild
        while temp.leftchild is not None:
          temp = temp.leftchild
        temp_val = temp.value
        
        # swap current value with the value we need to replace, and then remove the value from current.rightchild
        root.value = temp_val
        root.rightchild = self.__recursive_remove(root.rightchild, temp_val)
        root.setheight()
      
    root.setheight()
    return Binary_Search_Tree.__balance(root)

    
  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    self.__root.leftchild = self.__recursive_remove(self.get_root(),value)
    if(self.get_root() is None):
      self.__set_height_of_root(0)
    else:
      self.__set_height_of_root(self.get_root().getheight())
  
  
  # private method for in_order()
  def inorderstring(self, root, list):
    if root:
      self.inorderstring(root.leftchild, list)
      
      list.append(str(root.value))

      self.inorderstring(root.rightchild, list)
    
    
  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    a = []
    self.inorderstring(self.get_root(), a)
    if(len(a) == 0):
      return "[ ]"
    else:
      string = "[ "
      for i in range(0, len(a)-1):
        string += str(a[i]) + ", "
      string += a[len(a)-1] + " ]"
      return string


  # private method for pre_order()
  def __pre_trav(self, root, list):
    if root:
      list.append(str(root.value))
      
      self.__pre_trav(root.leftchild, list)

      self.__pre_trav(root.rightchild, list)
    
    
  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    a = []
    self.__pre_trav(self.get_root(), a)
    if(len(a) == 0):
      return "[ ]"
    else:
      string = "[ "
      for i in range(0, len(a)-1):
        string += str(a[i]) + ", "
      string += a[len(a)-1] + " ]"
      return string


  # private mathod for post_order()
  def __post_trev(self, root, list):
    if root:
      self.__post_trev(root.leftchild, list)
      self.__post_trev(root.rightchild, list)
      list.append(str(root.value))
    
    
  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    a = []
    self.__post_trev(self.get_root(), a)
    if(len(a) == 0):
      return "[ ]"
    else:
      string = "[ "
      for i in range(0, len(a)-1):
        string += str(a[i]) + ", "
      string += a[len(a)-1] + " ]"
      return string


  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    # TODO replace pass with your implementation
    return self.height

    
  def __str__(self):
    return self.in_order()
    #return self.pre_order()
    #return self.post_order()

  def inorder_tolist(self, root, list):
    if root:
      self.inorder_tolist(root.leftchild, list)
      
      list.append(root.value)

      self.inorder_tolist(root.rightchild, list)
  
  def to_list(self):
    list = []
    self.inorder_tolist(self.get_root(), list)
    return list
   
if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.
