class Link(object):
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)
        
class Stack(object):
    def __init__(self):
        self.first = None

    def push(self,data):
        current = self.first
        if( current == None ):
            self.first = Link(data)
            self.first.next = None
            return
        while( current.next != None ):
            current = current.next
        current.next = Link(data)
        return

    def pop(self):
        current = self.first
        if( current == None ):
            return None
        if( current.next == None ):
            temp = current
            self.first = None
            return current
        while( current.next.next != None ):
            current = current.next
        temp = current.next
        current.next = None
        return temp

    def __str__(self):
        current = self.first
        if( current == None ):
            return ''
        a = ''
        while(current!=None):
            a += str(current)
            current = current.next
        return a

class Queue(object):
    def __init__(self):
        self.first = None

    def push(self,data):
        current = self.first
        if( current == None ):
            self.first = Link(data)
            self.first.next = None
            return
        while( current.next != None ):
            current = current.next
        current.next = Link(data)
        return

    def pop(self):
        current = self.first
        if( current == None ):
            return None
        if( current.next == None ):
            temp = current
            self.first = None
            return current
        temp = current
        self.first = current.next
        return temp

    def __str__(self):
        current = self.first
        if( current == None ):
            return ''
        a = ''
        while(current!=None):
            a += str(current)
            current = current.next
        return a

def main():
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st)
    print(st.pop())
    print(st)
    print(st.pop())
    print(st.pop())
    print(st)

    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q)
    print(q.pop())
    print(q)
    print(q.pop())
    print(q.pop())
    print(q)
main()

    
        
