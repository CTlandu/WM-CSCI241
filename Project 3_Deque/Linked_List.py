class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__size = 0
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        new_Node = self.__Node(val)
        self.__trailer.prev.next = new_Node
        new_Node.prev = self.__trailer.prev
        new_Node.next = self.__trailer
        self.__trailer.prev = new_Node
        self.__size += 1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        new_Node = self.__Node(val)
        if index < 0 or index >= self.__size:
            raise IndexError
        elif(index < self.__size/2):
            cur = self.__header.next
            for i in range(0,index):
                cur = cur.next
            cur.prev.next = new_Node
            new_Node.prev = cur.prev
            cur.prev = new_Node
            new_Node.next = cur
            self.__size += 1
        else:
            cur = self.__trailer.prev
            for i in range(self.__size-1,index,-1):
                cur = cur.prev
            cur.prev.next = new_Node
            new_Node.prev = cur.prev
            new_Node.next = cur
            cur.prev = new_Node
            self.__size += 1

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if(index < 0 or index >= self.__size):
            raise IndexError
        elif(index < self.__size/2):
            cur = self.__header.next
            for i in range(0, index):
                cur = cur.next
            value = cur.val
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            self.__size -= 1
            return value
        else:
            cur = self.__trailer.prev
            for i in range(self.__size-1,index,-1):
                cur = cur.prev
            value = cur.val
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            self.__size -= 1
            return value        
        

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if (index < 0 or index >= self.__size):
            raise IndexError
        elif index == 0:
            return self.__header.next.val
        elif index == self.__size-1:
            return self.__trailer.prev.val
        elif index < self.__size/2:
            cur = self.__header.next
            for i in range(0,index):
                cur = cur.next
            return cur.val
        else:
            cur = self.__trailer.prev
            for i in range(self.__size-1, index):
                cur = cur.prev
            return cur.val
            
                

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__size == 0 or self.__size == 1:
            return
        else:
            cur = self.__header.next
            cur.prev = self.__trailer.prev
            self.__trailer.prev.next = cur
            self.__header.next = cur.next
            cur.next.prev = self.__header
            cur.next = self.__trailer
        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        if self.__size == 0:
            return("[ ]")
        else:
            string = "["
            for i in self:
                string += (" " + str(i) + ",")
        string = string[0:len(string)-1]+ " ]"
        return string

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        #print("iter called. initializing iter_index to 0")
        self.current = self.__header
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.current.next == self.__trailer:
            raise StopIteration
        self.current = self.current.next
        return self.current.val
        
    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        newLL = Linked_List()
        cur = self.__trailer.prev
        while(cur is not self.__header):
            newLL.append_element(cur.val)
            cur = cur.prev
        return newLL
            

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    a = Linked_List()
    print(a)
    print('linked list has ' + str(len(a)) + ' elements')
    try:
        a.append_element(1)
        a.append_element(2)
        a.append_element(3)
        a.append_element(4)
    except IndexError:
        print("Error: Index Out of Bound or Negative")
    print(a)
    print('linked list has ' + str(len(a)) + ' elements')
    
    print("After a legal insertion: 5,0")
    try:
        a.insert_element_at(5,0)
    except IndexError:
        print("Error: Index Out of Bound or Negative")
    print(a)
    print('linked list has ' + str(len(a)) + ' elements')
    
    print("After illegal insertion: 5,6")
    try:
        a.insert_element_at(5,6)
        a.insert_element_at(5,-1)
    except IndexError:
        print("Error: Index Out of Bound or Negative")
    print(a)
    print('linked list has ' + str(len(a)) + ' elements')
    
    
    print("After legal removal: 0")
    try:
        a.remove_element_at(0)
    except IndexError:
        print("Error: Index Out of Bound or Negative")
    print(a)
    print('linked list has ' + str(len(a)) + ' elements')
    
    print("After illegal removal: 10")
    try:
        a.remove_element_at(10)
    except IndexError:
        print("Error: Index Out of Bound or Negative")
    print(a)
    print('linked list has ' + str(len(a)) + ' elements')
    
    print("for loop test:")
    for val in a:
        print(val)
    
    print("for loop test for reversed(a): ")  
    for val in reversed(a):
        print(val)
        
    print("test for rotation: ")
    a.rotate_left()
    print(a)
