names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']
## CREATE YOUR FUNCTION HERE

def sort_names(col):
    col.sort()
    return col 

print(sort_names(names))
