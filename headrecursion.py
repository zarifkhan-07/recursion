def head_recursion(n):
    if n == 0:
        return
    print("Before recursion:", n)
    head_recursion(n - 1)

def main():
    number = 5
    print("Head recursion output:")
    head_recursion(number)

main()
