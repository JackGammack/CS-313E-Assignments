#  File: ExpressionTree.py

#  Description: Evaluates an infix expression and prints
#               the prefix and postfix expressions

#  Student's Name: Jack Gammack

#  Student's UT EID: jg64475

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 513354

#  Date Created: 4/8/2018

#  Date Last Modified: 4/12/2018

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Node (object):
  def __init__ (self, data=None):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
      self.root = None

  def createTree (self, expr):
    st = Stack()
    expr = expr.split()
    self.root = Node()
    current = self.root
    for item in expr:
      if( item == '(' ):
        current.lChild = Node()
        st.push(current)
        current = current.lChild
      elif( item == '+' or item == '-' or item == '*' or item == '/' ):
        current.data = item
        st.push(current)
        current.rChild = Node()
        current = current.rChild
      elif( item == ')' and not st.isEmpty() ):
        current = st.pop()
      elif( st.isEmpty() ):
        continue
      else:
        current.data = item
        current = st.pop()

  def evaluate (self, aNode):
    if( aNode != None ):
        if( aNode.data == '+' ):
            a = self.evaluate( aNode.lChild )
            b = self.evaluate( aNode.rChild )
            return a + b
        elif( aNode.data == '-' ):
            a = self.evaluate( aNode.lChild )
            b = self.evaluate( aNode.rChild )
            return a - b 
        elif( aNode.data == '*' ):
            a = self.evaluate( aNode.lChild )
            b = self.evaluate( aNode.rChild )
            return a * b 
        elif( aNode.data == '/' ):
            a = self.evaluate( aNode.lChild )
            b = self.evaluate( aNode.rChild )
            return a / b
        else:
            return float(aNode.data)

  def preOrder (self, aNode):
    if( aNode != None ):
      if( aNode.data == '+' or aNode.data == '-' or aNode.data == '*' or aNode.data == '/' ):
        a = self.preOrder( aNode.lChild )
        b = self.preOrder( aNode.rChild )
        return aNode.data + ' ' + a + ' ' + b
      else:
        return aNode.data

  def postOrder (self, aNode):
    if( aNode != None ):
      if( aNode.data == '+' or aNode.data == '-' or aNode.data == '*' or aNode.data == '/' ):
        a = self.postOrder( aNode.lChild )
        b = self.postOrder( aNode.rChild )
        return a + ' ' + b + ' ' + aNode.data
      else:
        return aNode.data

def main():
    in_file = open('expression.txt','r')
    exp = in_file.readline().rstrip('\n')
    in_file.close()
    t = Tree()
    t.createTree(exp)
    eva = t.evaluate(t.root)
    if( abs( eva - int(eva) ) < 0.0000001 ):
      eva = int(eva)
    eva = str(eva)
    print(exp + ' = ' + eva)
    print()
    print('Prefix Expression: ' , end = '' )
    pre = t.preOrder(t.root)
    print( pre )
    print('\n')
    print('Postfix Expression: ' , end = '' )
    post = t.postOrder(t.root)
    print(post)

main()
