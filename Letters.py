def permute(a,lo):
    hi = len(a)
    if( lo==hi ):
        if ( abs(a.index('A')-a.index('B')) > 1 ):
            return
        if ( abs(a.index('C')-a.index('D')) > 1 ):
            print(a)
    else:
        for i in range(lo,hi):
            a[lo],a[i]=a[i],a[lo]
            permute(a,lo+1)
            a[lo],a[i]=a[i],a[lo]

def main():
    l = ['A','B','C','D','E']
    permute(l,0)

main()
            
