from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  def push_front(self, val):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    pass
  
  def pop_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    pass

  def peek_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    pass

  def push_back(self, val):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    pass
  
  def pop_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    pass

  def peek_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    pass

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
