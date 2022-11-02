from inspect import stack
from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    # TODO replace pass with your implementation.
    # Orient your string from top (left) to bottom (right).
    return str(self.__dq)

  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self.__dq)

  def push(self, val):
    # TODO replace pass with your implementation.
    return self.__dq.push_front(val)

  def pop(self):
    # TODO replace pass with your implementation.
    return self.__dq.pop_front()

  def peek(self):
    # TODO replace pass with your implementation.
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  # a = Stack()
  # a.push(1)
  # a.push(2)
  # a.push(3)
  # a.push(4)
  # a.push(5)
  # print(a)
