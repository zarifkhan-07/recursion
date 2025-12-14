def sort(a):
    length=len(a)
    if length==1 or length==0:
        return True
    return a[0]<=a[1] and sort(a[1:])

a=[1,2,6,4,5,6]

if sort(a):
    print("The list is sorted.")
else:
    print("The list is not sorted.")