import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
    def setUp(self):
        self.__deque = get_deque(0)
        self.__stack = Stack()
        self.__queue = Queue()

    def test_empty_deque_and_stack_and_queue_string(self):
            self.assertEqual('[ ]', str(self.__deque))
            self.assertEqual('[ ]', str(self.__stack))
            self.assertEqual('[ ]', str(self.__queue))

    def test_empty_deque_and_stack_and_queue_length(self):
            self.assertEqual(0, len(self.__deque))
            self.assertEqual(0, len(self.__stack))
            self.assertEqual(0, len(self.__queue))

    def test_push_one_element_to_the_front_of_stack_and_deque(self):
            self.__deque.push_front(1)
            self.assertEqual('[ 1 ]', str(self.__deque))
            self.__stack.push(1)
            self.assertEqual('[ 1 ]', str(self.__stack))

    def test_push_one_element_to_the_back_of_deque_and_queue(self):
            self.__deque.push_back(1)
            self.__queue.enqueue(2)
            self.assertEqual('[ 1 ]', str(self.__deque))
            self.assertEqual('[ 2 ]', str(self.__queue))

    def test_one_element_length_of_stack_and_and_queue_deque(self):
            self.__deque.push_front(1)
            self.__queue.enqueue(2)
            self.__stack.push(3)
            self.assertEqual(1, len(self.__deque))
            self.assertEqual(1, len(self.__stack))
            self.assertEqual(1, len(self.__queue))
    
    def test_pop_front_empty_deque(self):
            try:
                self.__deque.pop_front()
            except:
                print("Cannot pop front the empty deque")
                
    def test_pop_back_empty_deque(self):
            try:
                self.__deque.pop_back()
            except:
                print("Cannot pop back the empty deque")
    
    def test_pop_empty_stack(self):
            try:
                self.__stack.pop()
            except:
                print("Cannot pop the empty stack")
             
    def test_pop_empty_queue(self):
            try:
                self.__queue.dequeue()
            except:
                print("Cannot dequeue the empty queue")
              
    def test_pop_one_element_from_the_front_of_stack_and_deque_and_queue(self):
            self.__deque.push_front(1)
            self.__stack.push(2)
            self.__queue.enqueue(3)
            self.__deque.pop_front()
            self.__stack.pop()
            self.__queue.dequeue()
            self.assertEqual('[ ]', str(self.__deque))
            self.assertEqual('[ ]', str(self.__stack))
            self.assertEqual('[ ]', str(self.__queue))
            
    def test_pop_one_element_from_the_back_of_deque(self):
            self.__deque.push_front(1)
            self.__deque.pop_back()
            self.assertEqual('[ ]', str(self.__deque))
    
    def test_peek_front_one_element(self):
            self.__deque.push_front(1)
            self.__stack.push(2)
            self.__queue.enqueue(3)
            returned1=self.__deque.peek_front()
            returned2=self.__stack.peek()
            returned3=self.__queue.peek()
            self.assertEqual(1, returned1)
            self.assertEqual(2, returned2)
            self.assertEqual(3, returned3)
    
    def test_peek_back_one_element(self):
            self.__deque.push_front(1)
            returned1=self.__deque.peek_back()
            self.assertEqual(1, returned1)
         
    def test_three_elements_length_of_stack_and_queue_and_deque(self):
            self.__deque.push_front(1)
            self.__stack.push(2)
            self.__queue.enqueue(3)
            self.__deque.push_back(2)
            self.__stack.push(3)
            self.__queue.enqueue(4)
            self.__deque.push_front(3)
            self.__stack.push(4)
            self.__queue.enqueue(5)
            self.assertEqual(3, len(self.__deque))
            self.assertEqual(3, len(self.__stack))
            self.assertEqual(3, len(self.__queue))
    
    def test_three_elements_stack_and_queue_and_deque_string(self):
            self.__deque.push_front(1)
            self.__stack.push(2)
            self.__queue.enqueue(None)
            self.__deque.push_back(2)
            self.__stack.push(3)
            self.__queue.enqueue(4)
            self.__deque.push_back(None)
            self.__stack.push(4)
            self.__queue.enqueue(5)
            self.assertEqual('[ 1, 2, None ]', str(self.__deque))
            self.assertEqual('[ 4, 3, 2 ]', str(self.__stack))
            self.assertEqual('[ None, 4, 5 ]', str(self.__queue))
     
    def test_pop_front_one_element_from_three_elements_stack_and_queue_and_deque(self):
            self.__deque.push_front(1)
            self.__stack.push(2)
            self.__queue.enqueue(None)
            self.__deque.push_back(2)
            self.__stack.push(3)
            self.__queue.enqueue(4)
            self.__deque.push_back(None)
            self.__stack.push(4)
            self.__queue.enqueue(5)
            self.__deque.pop_front()
            self.__stack.pop()
            self.__queue.dequeue()
            self.assertEqual('[ 2, None ]', str(self.__deque))
            self.assertEqual('[ 3, 2 ]', str(self.__stack))
            self.assertEqual('[ 4, 5 ]', str(self.__queue))
            
    def test_pop_back_one_element_from_three_elements_stack_and_queue_and_deque(self):
            self.__deque.push_front(1)
            self.__deque.push_back(2)
            self.__deque.push_back(None)
            self.__deque.pop_back()
            self.assertEqual('[ 1, 2 ]', str(self.__deque))
            
    def test_pop_front_value_of_three_element(self):
            self.__deque.push_front(1)
            self.__stack.push(2)
            self.__queue.enqueue(None)
            self.__deque.push_back(2)
            self.__stack.push(3)
            self.__queue.enqueue(4)
            self.__deque.push_back(None)
            self.__stack.push(4)
            self.__queue.enqueue(5)
            returned1=self.__deque.peek_front()
            returned2=self.__stack.peek()
            returned3=self.__queue.peek()
            self.assertEqual(1, returned1)
            self.assertEqual(4, returned2)
            self.assertEqual(None, returned3)
            
    def test_pop_back_value_of_three_element(self):
            self.__deque.push_front(1)
            self.__deque.push_back(2)
            self.__deque.push_back(None)
            returned1=self.__deque.peek_back()
            self.assertEqual(None, returned1)
            
  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

if __name__ == '__main__':
    unittest.main(module='DSQ_Test')

