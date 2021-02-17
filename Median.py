def median(a):
    return modqsort(a,0,len(a)-1)

def modqsort(a,lo,hi):
    if(lo>=hi):
        return
    pivot = a[lo]
    m=lo
    for i in range(lo,hi+1):
        if(a[i]<pivot):
            m=m+1
            a[m],a[i] = a[i],a[m]
    a[lo],a[m]=a[m],a[lo]
    if(m==(len(a)-1)//2):
        return a[m]
    if(m>(len(a)-1)//2):
        return modqsort(a,lo,m-1)
    if(m<(len(a)-1)//2):
        return modqsort(a,m+1,hi)
    return a[m]

def main():
    a = [3,5,1,2,4,6] #3
    print(median(a))
    a = [1,2,3,4,5,6] #3
    print(median(a))
    a = [1,2,3,4,5] #3
    print(median(a))
    a = [1,3,9,4,2] #3
    print(median(a))
    a = [9,4,3,1,2,6] #3
    print(median(a))
    a = [1,2,6,4,5,3] #3
    print(median(a))
    a = [1,2,4,5,6,7,3] #4
    print(median(a))
main()
    
