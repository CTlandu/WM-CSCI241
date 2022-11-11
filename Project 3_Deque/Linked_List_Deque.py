#from numpy import append
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

    # temp = Linked_List.Node(val)
    # temp.next = self.__list.__header.next
    # self.__list.__header.next.prev = temp
    # self.__list.__header.next = temp
    # temp.prev = self.__list.__header
    if(len(self.__list) == 0):
      self.__list.append_element(val)
    else:
      self.__list.insert_element_at(val,0)

  
  def pop_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self) == 0:
      return None
    return self.__list.remove_element_at(0)

  def peek_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self) == 0:
      return None
    return self.__list.get_element_at(0)

  def push_back(self, val):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    self.__list.append_element(val)
  
  def pop_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    if(len(self) == 0):
      return None
    return self.__list.remove_element_at(len(self.__list)-1)

  def peek_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    if(len(self)) == 0:
      return None
    return self.__list.get_element_at(len(self.__list)-1)

# Unit tests make the main section unneccessary.
if __name__ == '__main__':
  pass
#   def rec(D):
#       if len(D) == 0:
#         return D
#       if len(D) == 1:
#         return D
#       else:
#         val = D.pop_back()
#         rec(D).push_front(val)
#         return D
    
#   dq=Linked_List_Deque()
#   dq.push_back('A')
#   dq.push_back('B')
#   dq.push_back('C')
#   dq.push_back('D')
#   dq.push_back('E')
#   print(rec(dq))
