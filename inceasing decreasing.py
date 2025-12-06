def indec(n,num):
    if (n<1 or n>num):
        return
    print(n)
    indec(n-1,num)
    print(n)
num=int(input("Enter the number n:"))
indec(num,num)