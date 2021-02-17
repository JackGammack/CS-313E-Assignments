#  File: BST_Cipher.py

#  Description: encrypts and decrypts messages

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 4/13/2018

#  Date Last Modified: 4/18/2018

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

  def __str__ (self):
    return str(self.data)

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
      self.root = None
      for char in encrypt_str:
          if( ord(char) == 32 or ( ord(char) >= 97 and ord(char) <= 122 ) ):
              self.insert( char )

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
      new_node = Node( ch )
      if( self.root == None ):
          self.root = new_node
      else:
          current = self.root
          parent = self.root
          while( current != None ):
              parent = current
              if( ch < current.data ):
                  current = current.lchild
              elif( ch > current.data ):
                  current = current.rchild
              else:
                  return
          if( ch < parent.data ):
              parent.lchild = new_node
          else:
              parent.rchild = new_node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
      st = ''
      current = self.root
      if( current == None ):
          return ''
      if( current.data == ch ):
          return '*'
      while( current != None ):
          if( ch < current.data ):
              st += '<'
              current = current.lchild
          elif( ch > current.data ):
              st += '>'
              current = current.rchild
          else:
              break
      if( current == None ):
          return ''
      return st

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
      current = self.root
      if( st == '*' ):
          return current.data
      for char in st:
          if( current == None ):
              return ''
          if( char == '<' ):
              current = current.lchild
          else:
              current = current.rchild
      if( current == None ):
          return ''
      return current.data

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
      enc = ''
      st = st.lower()
      for char in st:
          a = self.search(char)
          if( len(a) != 0 ):
              enc = enc + self.search(char) + '!'
      return enc[0:-1]

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
      dec = ''
      i = 0
      while( i < len(st) ):
          indexc = i
          while( indexc != len(st) and st[indexc] != '!' ):
              indexc += 1
          dec = dec + self.traverse( st[i:indexc] )
          i = indexc + 1
      return dec

def main():
  a = input( 'Enter encryption key: ' )
  print()
  t = Tree(a)
  b = input( 'Enter string to be encrypted: ' )
  print( 'Encrypted string: ' + t.encrypt(b) )
  print()
  c = input( 'Enter string to be decrypted: ' )
  print( 'Decrypted string: ' + t.decrypt(c) )
  

main()
