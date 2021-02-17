def main():
  n=5
  square = []
  for i in range(n):
      square.append([0]*n)
  square[n-1][n//2]=1

  r = n-1
  c = n//2
  for i in range(2,n*n+1):
    if ( r+1 < n and c+1 < n ):
      if ( square[r+1][c+1] == 0 ):
        square[r+1][c+1] = i
        r = r+1
        c = c+1
        continue
      elif ( r-1 >= 0 ):
        square[r-1][c] = i
        r = r-1
        continue
      else:
        square[n-1][c] = i
        r = n-1
        continue
    if ( r+1 == n and c+1 == n ):
      if ( square[0][0] == 0 ):
          square[0][0] = i
          r = 0
          c = 0
          continue
      else:
          square[r-1][c] = i
          r = r-1
          continue
    if ( r+1 == n ):
      if ( square[0][c+1] == 0 ):
        square[0][c+1] = i
        r = 0
        c = c+1
        continue
      else:
        square[r-1][c] = i
        r = r-1
        continue
    if ( c+1 == n ):
      if ( square[r+1][0] == 0 ):
        square[r+1][0] = i
        r = r+1
        c = 0
        continue
      elif ( r-1 == -1 ):
        square[n-1][c] = i
        r = n-1
        continue
      else:
        square[r-1][c] = i
        r = r-1
        continue
  print(square)

  n = len(square)
  mx = n*n
  dig = len( str(mx) )
  for r in range(n):
    row = ''
    for c in range(n):
      l = len( str(square[r][c]) )
      row += ' '*(dig-l) + str(square[r][c]) + '  '
    print(row)
     
main()
