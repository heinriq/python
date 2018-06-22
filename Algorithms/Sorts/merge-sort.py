def merge(a,b):
    c = []

    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    
    if len(a) == 0:
        c += b
    else:
        c += a
    
    return c

def mergesort(x):
    
    if len(x) <= 1:
        return x
    else:
        a = mergesort(x[:len(x)/2])
        b = mergesort(x[len(x)/2:])
    return merge(a,b)

sorted = mergesort([1,4,2,3,6,4,5,7,0,9,8,0,1,21,11,13,14,10])
print(sorted)