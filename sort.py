def sort(a):
    n = len(a)
    for i in range(0, n):
        j = n-1
        while j > i :
            if a[j] < a[j-1] :
                t = a[j]
                a[j] = a[j-1]
                a[j-1] = t
            j = j -1
        i= i + 1
    return a
print(sort([1,3,5,2,4,5,6]))
