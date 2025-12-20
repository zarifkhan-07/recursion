def maze_paths(r, c, path):
    if r == 1 and c == 1:
        print(path)
        return
    
    if c > 1:
        maze_paths(r, c - 1, path + "r")
    
    if r > 1:
        maze_paths(r - 1, c, path + "d")


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

maze_paths(rows, cols, "")
