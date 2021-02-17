class Link(object):
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.data)

class DoublyLinked(object):
    def __init__(self):
        self.first = None
        
    def insert_first(self,data):
        current = self.first
        if( current == None ):
            self.first = Link(data)
            self.first.next = None
            self.first.prev = None
            return
        self.first = Link(data)
        self.first.prev = None
        self.first.next = current
        current.prev = self.first
        
    def remove(self,data):
        current = self.first
        if( current == None ):
            return None
        while( current!=None ):
            if( current.data == data ):
                if( current.prev == None and current.next == None ):
                    self.first = None
                    return
                if( current.prev == None ):
                    self.first = current.next
                    self.first.prev = None
                    return
                if( current.next == None ):
                    current.prev.next = None
                    return
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next
        return None
    
    def __str__(self):
        a = ''
        current = self.first
        if( current == None ):
            a += 'None'
        while(current.next!=None):
            a += str(current.data) + '  '
            current = current.next
        a += str(current.data) + '  '
        while( current!=None):
            a += str(current.data) + '  '
            current = current.prev
        return a

def main():
    dl = DoublyLinked()
    dl.insert_first(1)
    dl.insert_first(2)
    dl.insert_first(3)
    dl.insert_first(4)
    dl.insert_first(5)
    print(dl)
    dl.remove(1)
    dl.remove(3)
    dl.remove(5)
    dl.remove(6)
    print(dl)

main()
