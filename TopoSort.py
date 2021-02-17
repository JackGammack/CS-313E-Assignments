#  File: TopoSort.py

#  Description: Tests if a graph has a cycle and performs topological sort

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 4/28/2018

#  Date Last Modified: 5/4/2018

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

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # get a list of immediate neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, i):
      neighbours = []
      nVert = len( self.Vertices )
      for j in range( nVert ):
          if( self.getEdgeWeight( i,j ) != -1 ):
              neighbours.append( j )              
      return neighbours

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
      
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

      # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, i,j):
      if( self.adjMat[i][j] == 0 ):
          return -1
      return self.adjMat[i][j]

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  def getAdjVertex ( self, v ):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0):
        return i
    return -1

  def hasCycle_helper( self, i, onStack ):
    onStack[i] = True
    self.Vertices[i].visited = True
    neighbors = self.getNeighbors(i)
    for neighbor in neighbors:
      if( (not self.Vertices[neighbor].visited) and self.hasCycle_helper( neighbor, onStack ) ):
        return True
      elif( onStack[neighbor] == True ):
        return True
    onStack[i] = False
    return False
      
  # determine if a directed graph has a cycle
  def hasCycle (self):
      onStack = [False] * len( self.Vertices )
      
      for i in range( len( self.Vertices ) ):
        if( (not self.Vertices[i].visited) and self.hasCycle_helper(i,onStack) ):
          for item in self.Vertices:
            item.visited = False
          return True
      for item in self.Vertices:
        item.visited = False
      return False
    
  def toposort_helper(self,i,stack):
      self.Vertices[i].visited = True
      while( self.getAdjUnvisitedVertex(i) != -1 ):
          self.toposort_helper( self.getAdjUnvisitedVertex(i) ,stack)
      stack.push(i)
          
  # return a list of vertices after a topological sort
  def toposort (self):
      theStack = Stack()
      for i in range( len( self.Vertices ) ):
          if( not self.Vertices[i].visited ):
              self.toposort_helper(i,theStack)
      verts = []
      while( not theStack.isEmpty() ):
          a = theStack.pop()
          a = self.Vertices[a].getLabel()
          verts.append( a )
      return verts

def main():
  # create a Graph object
  dag = Graph()

  # open file for reading
  inFile = open ("./topo.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())
  print (numVertices)

  for i in range (numVertices):
    v = (inFile.readline()).strip()
    print (v)
    dag.addVertex (v)

  # read the edges
  numEdges = int ((inFile.readline()).strip())
  print (numEdges)

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    print (edge)
    edge = edge.split()
    start = dag.getIndex( edge[0] )
    finish = dag.getIndex( edge[1] )
    weight = 1

    dag.addDirectedEdge (start, finish, weight)

  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (numVertices):
    for j in range (numVertices):
      print (dag.adjMat[i][j], end = ' ')
    print ()
  print ()

  # close file
  inFile.close()


  # test if a directed graph has a cycle
  a = dag.hasCycle()
  print(dag.hasCycle())

  # test topological sort
  if( not a ):
    print( dag.toposort() )
  else:
    print( 'Has a cycle, cannot be toposorted' )
   
main()

