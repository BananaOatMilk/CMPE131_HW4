def merge_list(a, b):
    # checks if both are lists
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Both inputs must be lists")
    
    # check if all elements are ints
    for x in a + b:
        if isinstance(x, bool) or not isinstance(x, int):
            raise TypeError("All elements must be integers")
        
    # concatenate
    arr = a + b

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1 # start on the left of key
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] # move bigger elements to the right
            j -= 1 # moves left to the next element
        
        arr[j + 1] = key

    return arr