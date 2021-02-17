
# File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 4/2/2018

#  Date Last Modified: 4/7/2018

class Link (object):
  def __init__ (self, col = 0, data = 0, next = None):
    self.col = col
    self.data = data
    self.next = next

  # return a String representation of a Link (col, data)
  def __str__ (self):
    s = ''
    print( str( (self.col,self.data) ) )
    return s

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insert_last (self, col, data):
    new_link = Link (col, data)
    current = self.first

    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link

  def insert_link(self,col,data):
    current = self.first
    if( current == None ):
      self.first = Link(col,data)
      return
    if( current.col == col ):
      temp = current.next
      self.first = Link(col,data,temp)
      return
    if( current.col > col ):
      self.first = Link(col,data,current)
      return
    while( current.next != None ):
      if( current.next.col > col ):
        temp = current.next
        current.next = Link(col,data,temp)
        return
      if( current.next.col == col ):
        temp = current.next.next
        current.next = Link(col,data,temp)
        return
      current = current.next
    current.next = Link(col,data)
    return

  def delete_link(self,data):
    current = self.first
    if( current == None ):
      return None
    if( current.data == data ):
      temp = current
      self.first = current.next
      return current
    while( current.next != None ):
      if( current.next.data == data ):
        temp = current.next
        current.next = current.next.next
        return temp
      current = current.next
    return None

  # return a String representation of a LinkedList
  def __str__ (self):
    s = ''
    current = self.first
    if( current == None ):
        return s
    s += str((current.col,current.data))
    current = current.next
    while( current != None ):
        s += ', ' + str((current.col,current.data))
        current = current.next
    return s

class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = []

  # perform assignment operation: matrix[row][col] = data
  def set_element (self, row, col, data):
    current = self.matrix[row].first
    if( current == None ):
        self.matrix[row].first = Link(col,data)
        return
    if( col == current.col ):
        self.matrix[row].first = Link(col,data,current.next)
        return
    if( col < current.col ):
        self.matrix[row].first = Link(col,data,current)
        return
    while( current.next != None ):
        if( col < current.next.col ):
            temp = current.next
            current.next = Link(col,data,temp)
            return
        if( col == current.next.col ):
            if( data == 0 ):
                current.next = current.next.next
                return
            current.next = Link(col,data,current.next.next)
            return
        current = current.next
    current.next = Link(col,data)
    return

  # add two sparse matrices
  def __add__ (self, other):
    if( self.col != other.col or self.row != other.row ):
        return None
    newmat = Matrix(self.row,self.col)
    for i in range(self.row):
        newmat.matrix.append(LinkedList())
    for i in range(self.row):
        r1 = self.get_row_LL(i)
        r2 = other.get_row_LL(i)
        curr1 = r1.first
        curr2 = r2.first
        while( curr1 != None and curr2 != None ):
            if( curr1.col == curr2.col ):
                newmat.set_element(i,curr1.col,curr1.data+curr2.data)
                curr1 = curr1.next
                curr2 = curr2.next
            elif( curr1.col < curr2.col ):
                newmat.set_element(i,curr1.col,curr1.data)
                curr1 = curr1.next
            else:
                newmat.set_element(i,curr2.col,curr2.data)
                curr2 = curr2.next
        if( curr2 != None ):
            newmat.set_element(i,curr2.col,curr2.data)
            curr2 = curr2.next
        if( curr1 != None ):
            newmat.set_element(i,curr1.col,curr1.data)
            curr1 = curr1.next
    return newmat

  # multiply two sparse matrices
  def __mul__ (self, other):
    if( self.col != other.row ):
        return None
    newmat = Matrix(self.row,other.col)
    for i in range(self.row):
        newmat.matrix.append(LinkedList())
    for i in range( newmat.row ):
        for j in range( newmat.col ):
            a = self.get_row_LL(i)
            b = other.get_col_LL(j)
            acurr = a.first
            bcurr = b.first
            if( acurr == None or bcurr == None ):
                continue
            sum = 0
            bind = 0
            while( acurr != None ):
                while( bind<acurr.col ):
                    bind += 1
                    bcurr = bcurr.next
                sum += acurr.data * bcurr.data
                acurr = acurr.next
                bcurr = bcurr.next
                bind += 1
            if( sum != 0 ):
                newmat.set_element(i,j,sum)
    return newmat

  # return a linked list representing a row
  def get_row (self, n):
    row_LL = self.matrix[n]
    i = 0
    row = []
    current = row_LL.first
    while( i < self.col ):
      if( current != None and i == current.col ):
        row.append( current.data )
        current = current.next
      else:
        row.append( 0 )
      i += 1
    return row
    
  def get_row_LL (self, n):
    return self.matrix[n]

  # return a linked list representing a column
  def get_col (self, n):
    column = []
    for i in range(self.row):
      column.append( self.get_row(i)[n] )
    return column

  def get_col_LL (self, n):
    c = LinkedList()
    for row in self.matrix:
        current = row.first
        while( current!=None ):
            if( current.col == n ):
                c_curr = c.first
                if( c_curr == None ):
                    c.first = Link(current.col,current.data)
                else:
                    while( c_curr.next != None ):
                        c_curr = c_curr.next
                    c_curr.next = Link(current.col,current.data)
                break
            if( current.col > n ):
                c_curr = c.first
                if( c_curr == None ):
                    c.first = Link(n,0)
                else:
                    while( c_curr.next != None ):
                        c_curr = c_curr.next
                    c_curr.next = Link(n,0)
                break
            current = current.next
        if( current == None ):
            c_curr = c.first
            if( c_curr == None ):
                c.first = Link(n,0)
            else:
                while( c_curr.next != None ):
                    c_curr = c_curr.next
                c_curr.next = Link(n,0)
    return c

  # return a String representation of a matrix
  def __str__ (self):
    s = ''
    max_len = 0
    for row in self.matrix:
        current = row.first
        while( current!=None ):
            a = len( str( current.data ) )
            if( max_len < a ):
                max_len = a
            current = current.next
    for row in self.matrix:
        current = row.first
        if( current == None ):
            s += (' ' * (max_len - 1) + '0' + ' ')*self.col + '\n'
            continue
        curr_col = 0
        while( current != None ):
            if( curr_col < current.col ):
                s += ' ' * (max_len - 1) + '0' + ' '
                curr_col += 1
                continue
            s += ' ' * (max_len - len( str( current.data ) )) + str(current.data) + ' '
            current = current.next
            curr_col += 1
        while( curr_col < self.col ):
            s += ' ' * (max_len - 1) + '0' + ' '
            curr_col += 1
        s += '\n'
    return s


def read_matrix (in_file):
  line = in_file.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = Matrix (row, col)

  for i in range (row):
    line = in_file.readline().rstrip("\n").split()
    new_row = LinkedList()
    for j in range (col):
      elt = int (line[j])
      if (elt != 0):
        new_row.insert_last(j, elt)
    mat.matrix.append (new_row)
  line = in_file.readline()

  return mat

def main():
  in_file = open ("./matrix.txt", "r")

  print ("Test Matrix Addition")
  matA = read_matrix (in_file)
  print (matA)
  matB = read_matrix (in_file)
  print (matB)
  
  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = read_matrix (in_file)
  print (matP)
  matQ = read_matrix (in_file)
  print (matQ)

  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.set_element (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Elements to a Zero Value")
  matB.set_element (1, 1, 0)
  print (matB)

  print ("\nTest Getting a Row")
  row = matP.get_row(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.get_col(0)
  print (col)
  
  in_file.close()

if __name__ == "__main__":
  main()
