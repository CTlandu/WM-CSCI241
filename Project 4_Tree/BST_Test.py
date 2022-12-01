from Binary_Search_Tree import Binary_Search_Tree

def test_insert():
  c = Binary_Search_Tree()
  c.insert_element(3)
  c.insert_element(1)
  c.insert_element(12)
  c.insert_element(0)
  c.insert_element(2)
  c.insert_element(7)
  c.insert_element(4)
  c.insert_element(15)
  c.insert_element(3.5)
  c.insert_element(3.2)
  c.insert_element(4.6)
  c.insert_element(5)
  c.insert_element(4.3)
  c.insert_element(5.3)

  #print(a.get_root())
  #print(c.get_root().value)
  print("--------")
  print(str(c))
  print(c.get_height())
  
def test_height():
  a = Binary_Search_Tree()
  a.insert_element(5)
  a.insert_element(3)
  a.insert_element(6)
  a.insert_element(2)
  a.insert_element(4)
  a.insert_element(3.5)
  a.insert_element(4.5)
  print("height of a: " + str(a.get_height()))

def test_remove():
  a = Binary_Search_Tree()
  a.insert_element(4)
  a.insert_element(1)
  a.insert_element(3)
  a.insert_element(2)
  a.insert_element(0)
  a.insert_element(8)
  a.insert_element(5)
  a.insert_element(9)
  a.insert_element(7)
  a.insert_element(6)
  a.insert_element(5.5)
  a.insert_element(4.5)
  
  a.remove_element(5)
  print("height of root: " + str(a.get_height()))
  print(str(a.get_root().getheight()))
  print(str(a))
  
def test_remove_root():
  a = Binary_Search_Tree() 
  a.insert_element(50)

  a.remove_element(50)
  print(a)
  print(a.get_height())

def test_ALV():
  a = Binary_Search_Tree()
  a.insert_element(5)
  a.insert_element(3)
  a.insert_element(6)
  a.insert_element(2)
  # a.insert_element(4)
  # a.insert_element(3.5)
  # a.insert_element(3.2)
  # a.insert_element(1)
  a.insert_element(2.5)
 # a.insert_element(0)
  print(a)
  print(a.get_height())
  print(str(a.get_root().value))
  print(str(a.get_root().leftchild.value))
  #print(str(a.get_root().leftchild.rightchild.value))
  

if __name__ == '__main__':
  #test_insert()
  #test_height()
  #test_remove()
  #test_remove_root()
  test_ALV()
