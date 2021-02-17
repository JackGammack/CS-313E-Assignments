#File: MagicSquare.py

#Description: Creates of magic square of odd dimensions

#Student's Name: Jack Gammack

#Student's UT EID: jg64475
 
#Partner's Name:

#Partner's UT EID:

#Course Name: CS 313E 

#Unique Number: 51335

#Date Created: 1/23/2018

#Date Last Modified: 1/26/2018

# Populate a 2-D list with numbers from 1 to n2
def make_square ( n ):
  #Fill an nxn 2D list with 0s and put a 1 in the bottom middle
  square = []
  for i in range(n):
      square.append([0]*n)
  square[n-1][n//2]=1

  #Use the algorithm to fill the rest
  r = n-1
  c = n//2
  for i in range(2,n*n+1):
    if ( square[ (r+1)%n ][ (c+1)%n ] != 0 ):
      r = (r-1)%n
      square[r][c] = i
    else:
      r = (r+1)%n
      c = (c+1)%n
      square[r][c] = i
  return square
     
    
# Print the magic square in a neat format where the numbers
# are right justified
def print_square ( magic_square ):
  n = len(magic_square)
  mx = n*n
  dig = len( str(mx) )
  #Add enough spaces to make each number string the same length
  for r in range(n):
    row = ''
    for c in range(n):
      l = len( str(magic_square[r][c]) )
      row += ' '*(dig-l) + str(magic_square[r][c]) + '  '
    print(row)

      
# Check that the 2-D list generated is indeed a magic square
def check_square ( magic_square ):
  #Check that rows are all the same
  s1 = sum( magic_square[0] )
  for item in magic_square:
    if ( s1 != sum(item) ):
      print( 'Not a magic square.' )
      break
  print( 'Sum of row = ' + str(s1) )

  #Check that columns are all the same
  n = len( magic_square )
  for c in range(n):
    s2 = 0
    for r in range(n):
      s2 += magic_square[r][c]
    if ( s2 != s1 ):
      print( 'Not a magic square.' )
      break
  print ( 'Sum of column = ' + str(s2) )

  #UL to LR diagonal
  s3 = 0
  for i in range(n):
    s3 += magic_square[i][i]
  if ( s3 != s1 ):
    print( 'Not a magic square.' )
  else:
    print( 'Sum diagonal (UL to LR) = ' + str(s3) )

  #UR to LL diagonal
  s4 = 0
  for i in range(n):
    s4 += magic_square[n-1-i][i]
  if ( s4 != s1 ):
    print( 'Not a magic square.' )
  else:
    print( 'Sum diagonal (UR to LL) = ' + str(s4) )
  
        
        

def main():
  # Prompt the user to enter an odd number 3 or greater
  # Check the user input
  n = 0
  while( not str(n).isdigit() or n<3 or n%2==0 ):
    try:
      n = int( input( 'Please enter an odd number: ') )
    except:
      n = 0
  # Create the magic square
  square = make_square(n)
  # Print the magic square
  print()
  print( 'Here is a ' + str(n) +' x ' + str(n) + ' magic square: ' )
  print()
  print_square( square )
  print()
  # Verify that it is a magic square
  check_square( square )

main()
