#  File: Triangle.py

#  Description: Calculates greatest sum of route through a triangle

#  Student's Name: Jack Gammack

#  Student's UT EID: jg64475

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51335

#  Date Created: 3/4/18

#  Date Last Modified: 3/9/18

import time

def paths(grid,r,c):
    if(r==len(grid)-1):
        return [[grid[r][c]]]
    else:
        futpaths = paths(grid,r+1,c) + paths(grid,r+1,c+1)
        totalpaths = []
        for item in futpaths:
            totalpaths += [[grid[r][c]] + item]
        return totalpaths
    
def height2sum(grid, row, column):
    if( row == len(grid)-2 ):
        if( grid[row+1][column] > grid[row+1][column+1] ):
            return grid[row][column] + grid[row+1][column]
        else:
            return grid[row][column] + grid[row+1][column+1]
    elif ( height2sum(grid,row+1,column) > height2sum(grid,row+1,column+1) ):
        return grid[row][column] + height2sum(grid,row+1,column)
    else:
        return grid[row][column] + height2sum(grid,row+1,column+1)
    
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):  
  sums = []
  for item in paths(grid,0,0):
      sums.append( sum(item) )
  return max(sums)

# returns the greatest path sum using greedy approach
def greedy (grid):
  sum = grid[0][0]
  c = 0
  for i in range( len(grid)-1 ):
      if( grid[i+1][c] > grid[i+1][c+1] ):
          sum += grid[i+1][c]
      else:
          sum += grid[i+1][c+1]
          c = c+1
  return sum

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
  return height2sum(grid,0,0)     

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  for r in range( len(grid)-1 ):
      for c in range( len(grid[len(grid)-2-r]) ):
          if ( grid[len(grid)-1-r][c] > grid[len(grid)-1-r][c+1] ):
              grid[len(grid)-2-r][c] += grid[len(grid)-1-r][c] 
          else:
              grid[len(grid)-2-r][c] += grid[len(grid)-1-r][c+1]
  print(grid)
  return [grid[0][0],grid]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  triangle = open('triangle.txt','r')
  size = int( triangle.readline().strip() )
  grid = []
  for i in range(size):
      row = triangle.readline().split()
      introw = []
      for j in range( len(row) ):
          introw.append( int( row[j] ) )
      grid.append(introw)
  return grid

def main ():
  # read triangular grid from file
  grid = read_file()

  ti = time.time()
  # output greates path from exhaustive search
  largest = exhaustive_search(grid)
  print('The greatest path sum through exhaustive search is ' + str(largest) + '.')
  tf = time.time()
  del_t = tf - ti
  # print time taken using exhaustive search
  print('The time taken for exhaustive search is ' + str(del_t) + ' seconds.')
  print()

  ti = time.time()
  # output greates path from greedy approach
  largest = greedy(grid)
  print('The greatest path sum through greedy search is ' + str(largest) + '.')
  tf = time.time()
  del_t = tf - ti
  # print time taken using greedy approach
  print('The time taken for greedy approach is ' + str(del_t) + ' seconds.')
  print()

  ti = time.time()
  # output greates path from divide-and-conquer approach
  largest = rec_search(grid)
  print('The greatest path sum through recursive search is ' + str(largest) + '.')
  tf = time.time()
  del_t = tf - ti
  # print time taken using divide-and-conquer approach
  print('The time taken for recursive search is ' + str(del_t) + ' seconds.')
  print()

  ti = time.time()
  # output greates path from dynamic programming
  largest = dynamic_prog(grid)
  print('The greatest path sum through dynamic programming is ' + str(largest[0]) + '.')
  tf = time.time()
  del_t = tf - ti
  # print time taken using dynamic programming
  print('The time taken for dynamic programming is ' + str(del_t) + ' seconds.')


if __name__ == "__main__":
  main()
