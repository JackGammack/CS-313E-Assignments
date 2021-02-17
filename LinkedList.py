class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
  def __str__(self):
      return str(self.data)

class LinkedList (object):
    def __init__ (self):
        self.first = None

    def insertFirst (self, data):
        newLink = Link (data)
        newLink.next = self.first
        self.first = newLink

    def insertLast (self, data):
        newLink = Link (data)
        current = self.first

        if (current == None):
            self.first = newLink
            return

        while (current.next != None):
            current = current.next

        current.next = newLink

    def findLink (self, data):
        current = self.first
        if (current == None):
            return None

        while (current.data != data):
            if(current.next == None):
                return None
            else:
                current = current.next

        return current

    def deleteLink (self, data):
        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next
        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    def __str__(self):
        current = self.first
        a = ''
        if(current==None):
            a += str(current)
        while(current!=None):
            a += str(current)
            current = current.next
        return a

def main():
    a = LinkedList()
    a.insertLast(2)
    a.insertFirst(1)
    a.insertLast(3)
    print(a)
    a.deleteLink(1)
    print(a)
    a.deleteLink(1)
    print(a)
main()
