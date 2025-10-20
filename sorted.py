def reverse_sort_dictionary(book: dict):
   
    if not isinstance(book, dict):
        raise TypeError("Input must be a dictionary")

    # sort the dictionary's (key, value) pairs by the key (name) in reverse
    items = sorted(book.items(), key=lambda kv: kv[0], reverse=True)

    # keep only (name, phone)  
    # the phone is value[0] from (phone, age)
    result = [(name, value[0]) for name, value in items]

    return result
