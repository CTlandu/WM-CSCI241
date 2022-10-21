from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    pass
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).
    pass
    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    pass

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    pass
    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    pass
    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    pass
    
  def peek_front(self):
    # TODO replace pass with your implementation.
    pass
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    pass
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    pass

  def peek_back(self):
    # TODO replace pass with your implementation.
    pass

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
