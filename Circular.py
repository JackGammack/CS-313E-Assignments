class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
  def __str__(self):
      return str(self.data)

class Circular(object):
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
  def __str__(self):
      current = self.first
      if( current == None ):
          return 'None'
      a = ''
      a += str(current.data) + '  '
      current = current.next
      while( current != self.first ):
          a += str(current.data) + '  '
          current = current.next
      a += str(current.data)
      return a
      

def main():
    cl = Circular()
    print(cl)
    cl.insert(1)
    print(cl)
    cl.insert(2)
    print(cl)
    cl.insert(3)
    print(cl)
    
    


main()
