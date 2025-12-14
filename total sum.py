def Totalsum(a):
    length=len(a)
    if len==1:
        return a[0]
    return a[0] + Totalsum(a[1:])
a=[1,2,3,4]
print("Sum is:",Totalsum)