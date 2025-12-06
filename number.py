def take_input():
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative number entered. Stopping...")
        return
    print("You entered:", num)
    take_input()   # recursive call

# Start the recursive input-taking process
take_input()
