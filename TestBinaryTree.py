#  File: TestBinaryTree.py

#  Description: Adds helper functions to the Tree class

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 4/13/2018

#  Date Last Modified: 4/14/2018

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # determine the size of the queue
  def size (self):
    return (len (self.queue))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

  def __str__ (self):
    return str(self.data)

class Tree (object):
  def __init__ (self):
    self.root = None

  # search for a node with a key
  def search (self, key):
    current = self.root
    while (current != None) and (current.data != key):
      if (key < current.data):
        current = current.lchild
      else:
        current = current.rchild
    return current

  # insert a node in a tree
  def insert (self, val):
    new_node = Node (val)

    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (val < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print (aNode.data)
      self.in_order(aNode.rchild)

  # pre order traversal - center, left, right
  def pre_order (self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.pre_order (aNode.lchild)
      self.pre_order (aNode.rchild)

  # post order traversal - left, right, center
  def post_order (self, aNode):
    if (aNode != None):
      self.post_order (aNode.lchild)
      self.post_order (aNode.rchild)
      print (aNode.data)

  # return the node with minimum value
  def min_node (self):
    current = self.root

    if (current == None):
      return None

    while (current.lchild != None):
      current = current.lchild

    return current



  # return the node with maximum value
  def max_node (self):
    current = self.root

    if (current == None):
      return None

    while (current.rchild != None):
      current = current.rchild

    return current
      

  # delete a node with a given key
  def delete (self, key):
    delete_node = self.root
    parent = self.root
    is_left = False

    # if empty tree
    if (delete_node == None):
      return None

    # find the delete node
    while (delete_node != None) and (delete_node.data != key):
      parent = delete_node
      if (key < delete_node.data):
        delete_node = delete_node.lchild
        is_left = True
      else:
        delete_node = delete_node.rchild
        is_left = False

    # if node not found
    if (delete_node == None):
      return None

    # check if delete node is a leaf node
    if (delete_node.lchild == None) and (delete_node.rchild == None):
       if (delete_node == self.root):
         self.root = None
       elif (is_left):
         parent.lchild = None
       else: 
         parent.rchild = None

    # delete node is a node with only a left child
    elif (delete_node.rchild == None):
      if (delete_node == self.root):
        self.root = delete_node.lchild
      elif (is_left):
        parent.lchild = delete_node.lchild
      else:
        parent.rchild = delete_node.lchild

    # delete node has both left and right children
    else:
      # find delete node's successor and the successor's parent node
      successor = delete_node.rchild
      successor_parent = delete_node

      while (successor.lchild != None):
        successor_parent = successor
        successor = successor.lchild

      # successor node is right child of delete node
      if (delete_node == self.root):
        self.root = successor
      elif (is_left):
        parent.lchild = successor
      else:
        parent.rchild = successor

      # connect delete node's left child to be the successor's left child
      successor.lchild = delete_node.lchild

      # successor node left descendant of delete node
      if (successor != delete_node.rchild):
        successor_parent.lchild = successor.rchild
        successor.rchild = delete_node.rchild

      return delete_node

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
      return self.is_similar_helper(self.root,pNode.root)

  def is_similar_helper (self,sNode,aNode):
      if( sNode == None and aNode == None ):
          return True
      if( sNode != None and aNode != None ):
          return (sNode.data == aNode.data) and self.is_similar_helper(sNode.lchild,aNode.lchild) and self.is_similar_helper(sNode.rchild,aNode.rchild)
      return False
    
  # Prints out all nodes at the given level
  def print_level (self, level):
      self.print_level_helper(self.root, level)
      print()

  def print_level_helper (self, aNode, level):
      if( aNode == None ):
          a = 1
      elif( level == 1 ):
          print( str(aNode.data) , end = ' ' )
      elif( level > 1 ):
          self.print_level_helper( aNode.lchild, level-1 )
          self.print_level_helper( aNode.rchild, level-1 )
                       

  # Returns the height of the tree
  def get_height (self):
      a = self.get_height_helper( self.root )
      if( a > 0 ):
          return a - 1
      return a

  def get_height_helper(self, aNode):
      if( aNode == None ):
          return 0
      else:
          return 1 + max( self.get_height_helper( aNode.lchild ), self.get_height_helper( aNode.rchild ) )

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
      return self.num_nodes_helper( self.root )

  def num_nodes_helper(self, aNode):
      if( aNode == None ):
          return 0
      return 1 + self.num_nodes_helper(aNode.lchild) + self.num_nodes_helper(aNode.rchild)

def main():
    # Create three trees - two are the same and the third is different
    t1 = Tree()
    t1.insert(50)
    t1.insert(30)
    t1.insert(70)
    t1.insert(10)
    t1.insert(40)
    t1.insert(60)
    t1.insert(80)
    t1.insert(7)
    t1.insert(25)
    t1.insert(38)
    t1.insert(47)
    t1.insert(58)
    t1.insert(65)
    t1.insert(77)
    t1.insert(96)
    

    t2 = Tree()
    t2.insert(50)
    t2.insert(30)
    t2.insert(70)
    t2.insert(10)
    t2.insert(40)
    t2.insert(60)
    t2.insert(80)
    t2.insert(7)
    t2.insert(25)
    t2.insert(38)
    t2.insert(77)
    t2.insert(96)
    t2.insert(65)
    t2.insert(47)
    t2.insert(58)
    
    t3 = Tree()
    t3.insert(51)
    t3.insert(30)
    t3.insert(70)
    t3.insert(10)
    t3.insert(40)
    t3.insert(60)
    t3.insert(80)
    t3.insert(7)
    t3.insert(25)
    t3.insert(38)
    t3.insert(47)
    t3.insert(58)
    t3.insert(65)
    t3.insert(77)
    t3.insert(96)
    t3.insert(59)

    t5 = Tree()
    t5.insert(5)

    t6 = Tree()
    # Test your method is_similar()
    print(t1.is_similar(t2))
    print(t1.is_similar(t3))
    print(t5.is_similar(t6))
    print(t6.is_similar(t6))
    # Print the various levels of two of the trees that are different
    t1.print_level(1)
    t1.print_level(2)
    t1.print_level(3)
    t1.print_level(4)
    t3.print_level(1)
    t3.print_level(2)
    t3.print_level(3)
    t3.print_level(4)
    t3.print_level(5)
    t5.print_level(1)
    t6.print_level(1)
    # Get the height of the two trees that are different
    print( t1.get_height() )
    print( t3.get_height() )
    print( t5.get_height() )
    print( t6.get_height() )
    # Get the total numbe of nodes a binary search tree
    print( t1.num_nodes() )
    print( t3.num_nodes() )
    print( t5.num_nodes() )
    print( t6.num_nodes() )

main()
