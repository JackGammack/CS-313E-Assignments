#  File: TestLinkedList.py

#  Description: Tests functions for linked lists

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 3/26/2018

#  Date Last Modified: 3/30/2018

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
  def __str__(self):
      return str(self.data)

class LinkedList (object):
  def __init__ (self):
      self.first = None
      
  # get number of links 
  def get_num_links (self):
      current = self.first
      ctr = 0
      while( current!=None ):
          ctr += 1
          current = current.next
      return ctr
  
  # add an item at the beginning of the list
  def insert_first (self, item):
      newLink = Link (item)
      newLink.next = self.first
      self.first = newLink

  # add an item at the end of a list
  def insert_last (self, item):
      newLink = Link (item)
      current = self.first
      if (current == None):
          self.first = newLink
          return
      while (current.next != None):
          current = current.next
      current.next = newLink

  # add an item in an ordered list in ascending order
  def insert_in_order (self, item):
      current = self.first
      if( current==None ):
          self.first = Link(item)
          return
      if( current.data >= item ):
          self.insert_first(item)
          return
      while( current.next!=None ):
          if( current.next.data >= item ):
              newLink = Link(item)
              newLink.next = current.next
              current.next = newLink
              return
          else:
              current = current.next
      current.next = Link(item)
      return

      
      
  # search in an unordered list, return None if not found
  def find_unordered (self, item):
    current = self.first
    if( current==None ):
        return None
    while( current!=None ):
        if( current.data == item ):
            return current
        current = current.next
    return None

  # Search in an ordered list, return None if not found
  def find_ordered (self, item):
    current = self.first
    if( current==None ):
        return None
    while( current!=None ):
        if( current.data == item ):
            return current
        if( current.data > item ):
            return None
        current = current.next
    return None

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, item):
    current = self.first
    if( self.find_unordered(item) == None ):
        return None
    if( current.data == item ):
        temp = self.first
        self.first = current.next
        return temp
    while( current != None and current.next!=None ):
        if( current.next.data == item ):
            temp = current.next
            current.next = current.next.next
            return temp
        current = current.next
    return None

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
      current = self.first
      a = ''
      if( current == None ):
          return ''
      newLine = ''
      while( current!=None ):
          while( len(newLine.split()) < 10 and current!=None ):
              newLine += str( current ) + '  '
              current = current.next
          if( len(newLine.split()) == 10 and current!=None ):
              a += newLine + '\n'
              newLine = ''
          else:
              a += newLine
              newLine = ''
      return a
          

  # Copy the contents of a list and return new list
  def copy_list (self):
    current = self.first
    newLinked = LinkedList()
    newLinked.first = self.first
    if( current == None ):
        return newLinked
    newLinked = LinkedList()
    newLinked.first = Link(self.first.data)
    newcurrent = newLinked.first
    current = current.next
    while( current!=None ):
        newcurrent.next = Link(current.data)
        newcurrent = newcurrent.next
        current = current.next
    return newLinked

  # Reverse the contents of a list and return new list
  def reverse_list (self):
    previous = None
    current = self.first
    if( current == None ):
      return self
    nxt = current.next
    if(current == None):
        return None
    while( current!=None ):
        current.next = previous
        previous = current
        current = nxt
        if(nxt!=None):
            nxt = nxt.next
    self.first = previous
    return self

  # Sort the contents of a list in ascending order and return new list
  def sort_list (self):
    unsrtd = self.copy_list()
    self.first = None
    current = unsrtd.first
    if( current == None ):
        return self
    while( current!=None ):
        self.insert_in_order(current.data)
        current = current.next
    return self

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first
    if ( current == None or current.next == None  ):
        return True
    current
    while( current.next!=None ):
      if( current.next.data < current.data ):
        return False
      current = current.next
    return True

  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    return ( self.first == None )

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other):
    comb = LinkedList()
    current = self.first
    while( current!= None ):
        comb.insert_in_order(current.data)
        current = current.next
    current = other.first
    while( current != None ):
        comb.insert_in_order(current.data)
        current = current.next
    return comb

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    scurrent = self.first
    ocurrent = other.first
    if( scurrent == None and ocurrent == None ):
        return True
    while( scurrent!=None and ocurrent!=None ):
        if( scurrent.data != ocurrent.data ):
            return False
        scurrent = scurrent.next
        ocurrent = ocurrent.next
    return ( scurrent == None and ocurrent == None )

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):
    current = self.first
    if( current == None or current.next == None):
        return self
    while( current!=None and current.next!=None ):
        if( current.data == current.next.data ):
            self.delete_link(current.data)
        current = current.next
    return self

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  one = LinkedList()
  one.insert_last(0)
  links = LinkedList()
  links.insert_first(12)
  links.insert_first(11)
  links.insert_first(10)
  links.insert_first(9)
  links.insert_first(8)
  links.insert_first(7)
  links.insert_first(6)
  links.insert_last(13)
  links.insert_first(5)
  links.insert_first(4)
  links.insert_first(3)
  links.insert_first(2)
  links.insert_first(1)
  print(links)
  empt = LinkedList()
  print(empt)
  # Test method insert_last()
  # Test method insert_in_order()
  lnks = LinkedList()
  lnks.insert_last(11)
  lnks.insert_in_order(7)
  lnks.insert_in_order(6)
  lnks.insert_in_order(8)
  lnks.insert_in_order(4)
  lnks.insert_in_order(9)
  lnks.insert_in_order(7)
  lnks.insert_in_order(10)
  lnks.insert_in_order(4)
  lnks.insert_first(3)
  print(lnks)
  print(one)
  # Test method get_num_links()
  print('Lengths:')
  print(one.get_num_links())
  print(links.get_num_links())
  print(lnks.get_num_links())
  print(empt.get_num_links())
  # Test method find_unordered() 
  # Consider two cases - item is there, item is not there
  print('Orders:')
  print(links.find_unordered(10))
  print(links.find_unordered(14))
  print(lnks.find_unordered(0))
  print(lnks.find_unordered(9))
  print(lnks.find_unordered(5))
  print(empt.find_unordered(0))
  print(one.find_unordered(1))
  print(one.find_unordered(0))
  # Test method find_ordered() 
  # Consider two cases - item is there, item is not there 
  print(links.find_ordered(10))
  print(links.find_ordered(14))
  print(links.find_ordered(5))
  print(lnks.find_ordered(5))
  print(lnks.find_ordered(12))
  print(empt.find_ordered(0))
  print(one.find_ordered(0))
  print(one.find_ordered(1))
  one.insert_first(2)
  # Test method delete_link()
  # Consider two cases - item is there, item is not there
  print('Deletes:')
  print(links.delete_link(9))
  print(links.delete_link(1))
  print(links.delete_link(13))
  print(links)
  print(lnks.delete_link(4))
  print(lnks.delete_link(6))
  print(lnks.delete_link(11))
  print(lnks.delete_link(6))
  print(lnks)
  print(empt.delete_link(0))
  print(empt)
  print(one.delete_link(2))
  print(one)
  print(one.delete_link(0))
  print(one)
  one.insert_first(0)
  lnks.insert_in_order(4)
  links.insert_first(10)
  print(links)
  print(lnks)
  print(one)
  print(empt)
  # Test method copy_list()
  print('Copies:')
  print(links.copy_list())
  print(lnks.copy_list())
  print(one.copy_list())
  print(empt.copy_list())
  print(links.insert_last(5))
  print(links.delete_link(10))
  print(links)
  print(links.is_sorted())
  # Test method reverse_list()
  print('Reversals:')
  print(links.reverse_list())
  print(lnks.reverse_list())
  print(one.reverse_list())
  print(empt.reverse_list())
  print(links)
  print(lnks)
  print(one)
  print(empt)
  print(links.is_sorted())
  print(lnks.is_sorted())
  print(one.is_sorted())
  print(empt.is_sorted())
  # Test method sort_list()
  print('Sorts:')
  print(links.sort_list())
  print(lnks.sort_list())
  print(one.sort_list())
  print(empt.sort_list())
  print(links)
  print(lnks)
  print(one)
  print(empt)
  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print('Sorted:')
  print(links.is_sorted())
  print(lnks.is_sorted())
  print(one.is_sorted())
  print(empt.is_sorted())
  # Test method is_empty()
  print('Empty:')
  print(links.is_empty())
  print(lnks.is_empty())
  print(one.is_empty())
  print(empt.is_empty())
  # Test method merge_list()
  print('Merge:')
  print(links.merge_list(lnks))
  print(lnks.merge_list(links))
  print(empt.merge_list(links))
  print(empt.merge_list(empt))
  print(one.merge_list(one))
  print(one.merge_list(lnks))
  print(lnks.merge_list(lnks))
  print(links)
  print(lnks)
  print(empt)
  print(one)
  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  two=LinkedList()
  two.insert_in_order(0)
  lanks = lnks.copy_list()
  print('Equals:')
  print(links.is_equal(lnks))
  print(links.is_equal(links))
  print(lnks.is_equal(links))
  print(lnks.is_equal(lnks))
  print(one.is_equal(two))
  print(empt.is_equal(empt))
  print(empt.is_equal(links))
  print(lnks.is_equal(lanks))
  lanks.insert_last(20)
  print(lnks.is_equal(lanks))
  # Test remove_duplicates()
  print('Duplicates:')
  print(links.remove_duplicates())
  print(lnks.remove_duplicates())
  print(empt.remove_duplicates())
  print(one.remove_duplicates())
  

if __name__ == "__main__":
  main()
