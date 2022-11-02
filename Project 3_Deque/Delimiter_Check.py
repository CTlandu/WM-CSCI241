import sys

from Stack import Stack # for sys.argv, the command-line arguments

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
  openfile = open(filename,"r")
  content = openfile.readlines()
  stack = Stack()
  
  meetdoublequote = False
  meetsinglequote = False
  for i in content:
    for j in i:
      if(j == "\"" ):
        if(meetdoublequote == False):
          meetdoublequote = True
          continue
        else:
          meetdoublequote = False
          continue
      elif(j == "\'" ):
        if(meetsinglequote == False):
          meetsinglequote = True
          continue
        else:
          meetsinglequote = False
          continue
      elif(meetdoublequote == True):
        continue
      elif(meetsinglequote == True):
        continue
      
      elif(j == "(" or j=="[" or j=="{"):
        stack.push(j)
      elif(j == ")"):
        if(stack.peek() != "("):
          return False
        else:
          stack.pop()
      elif(j == "]"):
        if stack.peek() != "[":
          return False
        else:
          stack.pop()
      elif(j == "}"):
        if stack.peek() != "{":
          return False
        else:
          stack.pop()
  print(content)
  if len(stack) == 0:
    return True    
  return False
        
        
if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


