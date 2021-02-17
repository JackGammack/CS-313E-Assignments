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

def permute(a,lo):
    hi = len(a)
    if(lo==hi):
        print(a)
    else:
        for i in range(lo,hi):
            a[lo],a[i] = a[i],a[lo]
            permute(a,lo+1)
            a[lo],a[i] = a[i],a[lo]

def combine(a,b,lo,size):
    hi = len(a)
    if(lo==hi):
        if(len(b)==size):
            print(b)
        return
    if(len(b)==size):
        print(b)
    else:
        c=b[:]
        b.append(a[lo])
        combine(a,b,lo+1,size)
        combine(a,c,lo+1,size)

def main():
  a = [1,2,3,4]
  b = []
  combine(a,b,0,1)

main()
