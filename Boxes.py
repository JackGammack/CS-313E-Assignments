#  File: Boxes.py

#  Description: Recursively finds the largest subset of nesting boxes

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 2/20/2018

#  Date Last Modified: 2/24/2018

max_len = 1
subs = []

def subsets (a, b, lo):
  global max_len
  global subs
  hi = len(a)
  #if we've tried every box, if subset b is bigger than or equal to others
  #append it
  if (lo == hi):
    if( len(b) >= max_len ):
        max_len = len(b)
        subs.append(b)
    return
  else:
    c = b[:]
    pos = len(b)-1
    #if no boxes yet, create one subset with the box and one without
    if( len(b) == 0 ):
        b.append(a[lo])
        subsets (a, b, lo + 1)
        subsets (a, c, lo + 1)
    #if last box fits in next box, create one subset with the box and one without
    elif( b[pos][0] < a[lo][0] and b[pos][1] < a[lo][1] and b[pos][2] < a[lo][2] ):
        b.append (a[lo])
        subsets (a, b, lo + 1)
        subsets (a, c, lo + 1)
    #else keep searching for next box
    else:
        subsets (a, b, lo + 1)
         
def main():
    infile = open('boxes.txt','r')
    numboxes = int( infile.readline() )
    boxes = []
    #sort boxes by increasing dimensions
    for i in range(numboxes):
        boxes.append( infile.readline().split() )
        boxes[i].sort()
        for j in range( len(boxes[i]) ):
            boxes[i][j] = int( boxes[i][j] )
    boxes.sort()
    subsets(boxes,[],0)
    global subs

    #add subsets that have max length
    largestsubs = []
    for i in range( len(subs) ):
        if( len(subs[i]) == max_len ):
            largestsubs.append( subs[i] )

    if( max_len == 1 ):
      print('No Nesting Boxes')
    else:
      print('Largest Subset of Nesting Boxes')
      for i in range( len(largestsubs) ):
        for j in range( max_len):
            print( largestsubs[i][j] )
        print()
    

main()
        
