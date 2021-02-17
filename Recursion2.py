
def selectionSort (a):
  for i in range (len(a) - 1):
    print(a)
    # find the minimum
    min = a[i]
    minIdx = i

    for j in range (i + 1, len(a)):
      if (a[j] < min):
        min = a[j]
        minIdx = j
    # Swap the minimum element with the element at the ith place
    a[minIdx] = a[i]
    a[i] = min

def bubbleSort1 (a):
  idx = 0
  while (idx < len(a) - 1):
    print(a)
    jdx = len(a) - 1
    while (jdx > idx):
      if (a[jdx] < a[jdx - 1]):
        a[jdx], a[jdx - 1] = a[jdx - 1], a[jdx]
      jdx = jdx - 1
    idx = idx + 1

def bubbleSort2 (a):
  swapped = True
  idx = 0
  while ((idx < len(a) - 1) and swapped):
    print(a)
    jdx = len(a) - 1
    swapped = False
    while (jdx > idx):
      if (a[jdx] < a[jdx - 1]):
        a[jdx], a[jdx - 1] = a[jdx - 1], a[jdx]
        swapped = True
      jdx = jdx - 1
    idx = idx + 1


def insertion_sort1 (a):
  for i in range (1, len(a)):
    print(a)
    j = i
    while ((j > 0) and (a[j] < a[j - 1])):
      a[j], a[j - 1] = a[j - 1], a[j]
      j += -1

def insertion_sort2 (a):
  for i in range (1, len(a)):
    tmp = a[i]
    j = i
    while ((j > 0) and (a[j - 1] > tmp)):
      a[j] = a[j - 1]
      j += -1
    a[j] = tmp


def sequentialSearch (a, x):
  for i in range (len(a)):
    if (a[i] == x):
      return i
  return -1

def binarySearch (a, x):
  lo = 0
  hi = len(a) - 1
  while (lo <= hi):
    mid = (lo + hi) // 2
    if (x > a[mid]):
      lo = mid + 1
    elif (x < a[mid]):
      hi = mid - 1
    else:
      return mid
  return -1

def merge (a, b):
  c = []
  idxA = 0
  idxB = 0

  while ((idxA < len(a)) and (idxB < len(b))):
    if (a[idxA] < b[idxB]):
      c.append (a[idxA])
      idxA = idxA + 1
    else:
      c.append (b[idxB])
      idxB = idxB + 1

  # if a is not empty write it out 
  while (idxA < len(a)):
    c.append (a[idxA])
    idxA = idxA + 1

  # if b is not empty write it out
  while (idxB < len(b)):
    c.append (b[idxB])
    idxB = idxB + 1

  return c

def mergeSort (a, left, right):
  if (left < right):
    center = (left + right) // 2
    mergeSort (a, left, center)
    mergeSort (a, center + 1, right)
    merge_sort (a, left, center, right)

def merge_sort (a, left, center, right):
  first1 = left
  last1 = center
  first2 = center + 1
  last2 = right
  b = []

  while ((first1 <= last1) and (first2 <= last2)):
    if (a[first1] < a[first2]):
      b.append(a[first1])
      first1 = first1 + 1
    else:
      b.append(a[first2])
      first2 = first2 + 1

  while (first1 <= last1):
    b.append(a[first1])
    first1 = first1 + 1

  while (first2 <= last2):
    b.append(a[first2])
    first2 = first2 + 1

  idxA = left
  for i in range (len(b)):
    a[idxA] = b[i]
    idxA = idxA + 1


def qsort1 (a, lo, hi):
  if (lo >= hi):
    return

  pivot = a[lo]
  m = lo;
  for i in range (lo, hi + 1):
    print(a)
    if (a[i] < pivot):
      m = m + 1
      a[m], a[i] = a[i], a[m]
  
  a[lo], a[m] = a[m], a[lo]
  print()
  qsort1 (a, lo, m - 1)
  qsort1 (a, m + 1, hi)

def qsort2 (a, lo, hi):
  if (lo >= hi):
    return

  left = lo
  right = hi
  pivot = a[(lo + hi) // 2]

  while (left < right):
    while (a[left] < pivot):
      left = left + 1
    while (pivot < a[right]):
      right = right - 1

    if (left <= right):
      a[left], a[right] = a[right], a[left]
      left = left + 1
      right = right - 1

  qsort2 (a, lo, right)
  qsort2 (a, left, hi)



def permute (a, lo, hi):
  if (lo == hi):
    print (a)
  else:
    for i in range (lo, hi):
      a[i], a[lo] = a[lo], a[i]
      permute (a, lo + 1, hi)
      a[i], a[lo] = a[lo], a[i]

def combine (a, b, idxA):
  if (idxA == len(a)):
    if (len(b) > 0):
      print (b)
      return
  else:
    c = b[:]
    b.append (a[idxA])
    idxA = idxA + 1
    combine (a, b, idxA)
    combine (a, c, idxA)


def subsets (a, b, lo):
  hi = len(a)
  if (lo == hi):
    print (b)
    return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, b, lo + 1)
    subsets (a, c, lo + 1)

def helper(start,nums,s1,s2):
    if( start == len(nums) ):
        return s1==s2
    else:
        if( nums[start]%5 == 0 ):
            return helper(start+1,nums,s1+nums[start],s2)
        if( nums[start]%3==0 ):
            return helper(start+1,nums,s1,s2+nums[start])
        return helper(start+1,nums,s1+nums[start],s2) or helper(start+1,nums,s1,s2+nums[start])

def main():
  print(helper(0,[1,1],0,0))
  print(helper(0,[1,1,1],0,0))
  print(helper(0,[2,4,2],0,0))

main()
