from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.size = 0
    self.front = 0
    self.back = 0
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).
    if self.size == 0:
      return("[ ]")
    elif (self.front <= self.back):
      string = "["
      for i in range(self.front, self.back+1):
        string += (" " + str(self.__contents[i]) + ",")
    else:    
      string = "["
      for i in range(self.front, len(self.__contents)):
        string += (" " + str(self.__contents[i]) + ",")
      for i in range(0, self.back+1):
        string += (" " + str(self.__contents[i]) + ",")
    string = string[0:len(string)-1]+ " ]"
    # string = ""
    # for i in self.__contents:
    #   string += str(i)
    return string
    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.size

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    # for i in range(self.__capacity):
    #   (self.__contents.insert(self.back+1,None))
    # if self.front > self.back:
    #   self.front += self.__capacity
    # self.__capacity *= 2
    self.__capacity = self.__capacity * 2
    new_array = [None] * self.__capacity
    if self.front<=self.back:
      for i in range(self.front, self.back+1):
        new_array[i-self.front] = self.__contents[i]
    else:
      index = 0
      for i in range(self.front,len(self.__contents)):
        new_array[index] = self.__contents[i]
        index += 1
      for i in range(0, self.back+1):
        new_array[index] = self.__contents[i]
        index += 1
    self.__contents = new_array
    self.front = 0
    self.back = self.size-1

    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.size >= self.__capacity:
      self.__grow()
    self.front = (self.front+self.__capacity-1)%self.__capacity
    self.__contents[self.front] = val
    self.size += 1
    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.size == 0:
      raise IndexError
    else:
      temp = self.__contents[self.front]
      self.front = (self.front+1)%self.__capacity
      self.size -= 1
      return temp
      
  def peek_front(self):
    # TODO replace pass with your implementation.
    return self.__contents[self.front] 
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.size >= self.__capacity:
      self.__grow()
    self.back = (self.back+1)%self.__capacity
    self.__contents[self.back] = val
    self.size += 1
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.size == 0:
      raise IndexError
    else:
      temp = self.__contents[self.back]
      self.back = (self.back+self.__capacity-1)%self.__capacity
      self.size -= 1
      return temp

  def peek_back(self):
    # TODO replace pass with your implementation.
    return self.__contents[self.back]
      
def rec(D):
  if len(D) == 0:
    return D
  if len(D) == 1:
    return D
  else:
    val = D.pop_back()
    rec(D).push_front(val)
    return D
# No main section is necessary. Unit tests take its place.
if __name__ == '__main__':
#  pass    
  dq=Array_Deque()
  dq.push_back('A')
  dq.push_back('B')
  dq.push_back('C')
  dq.push_back('D')
  dq.push_back('E')
  print(dq)
  print(rec(dq))

