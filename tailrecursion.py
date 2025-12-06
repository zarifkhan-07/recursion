def tailrect(a,num):
    if (a>num):
        return
    print(a)
    tailrect(a+1,num)
n=int(input("Enter n to print 1 to n:"))
tailrect(1,n)