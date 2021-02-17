#  File: Josephus.py

#  Description: Solve Josephus problem using circular linked list

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 3/26/2018

#  Date Last Modified: 4/2/2018

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
  def __str__(self):
      return str(self.data)

class CircularList(object):
  # Constructor
  def __init__ ( self ):
      self.first = None

  def insert ( self, item ):
      current = self.first
      if( current==None ):
          self.first = Link(item)
          current = self.first
          current.next = self.first
          return
      while( current.next.data!=self.first.data ):
          current = current.next
      current.next = Link(item)
      current = current.next
      current.next = self.first
      return

  # Find the link with the given key (value)
  def find ( self, key ):
      current = self.first
      if( current == None ):
          return None
      if( current.data == key ):
          return current
      else:
          current = current.next
      while( current.data != self.first.data ):
          if( current.data == key ):
              return current
          current = current.next
      return None

  # Delete a link with a given key (value)
  def delete ( self, key ):
      current = self.first
      if( self.find(key) == None ):
          return None
      while( True ):
          if( current.next.data == key ):
              if( current.next.data == self.first.data ):
                  temp = current.next.data
                  self.first = current.next.next
                  current.next = self.first
                  return temp
              temp = current.next.data
              current.next = current.next.next
              return temp
          current = current.next
      return None

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
      current = start
      for i in range(n-1):
          current = current.next
      temp = current.next
      self.delete( current.data )
      current = temp
      return current

  def find_after( self,start,n ):
      current = start
      for i in range(n-1):
        current = current.next
      return current

  # Return a string representation of a Circular List
  def __str__ ( self ):
      current = self.first
      a = ''
      if( current == None ):
          return ''
      a += str(current) + ' '
      current = current.next
      while( current.data != self.first.data ):
          a += str(current) + ' '
          current = current.next
      return a

def main():
    josephus = open('josephus.txt','r')
    numsoldiers = int(josephus.readline().strip())
    start = int(josephus.readline().strip())
    n = int(josephus.readline().strip())
    Circle = CircularList()
    for i in range(1, numsoldiers+1):
        Circle.insert(i)
    start = Circle.find(start)
    for i in range(numsoldiers-1):
        print( Circle.find_after(start,n) )
        start = Circle.delete_after(start,n)
    print(start)
main()
