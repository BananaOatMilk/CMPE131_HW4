def my_steps(n: int) -> int:  # takes int, returns int

    if isinstance(n, bool) or not isinstance(n, int) or not (1 <= n <= 25): # ensure n is an int and between [1-25]
        raise ValueError("n must be an integer between 1 to 25")
    # base cases
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    prev2 = 1
    prev1 = 2

    for _ in range (3, n + 1): # starts at 3, up to n
        temp = prev1 + prev2 # uses previous cases to solve current case
        prev2 = prev1
        prev1 = temp

    return prev1