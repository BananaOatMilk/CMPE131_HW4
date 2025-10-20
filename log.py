import time
from functools import wraps

def timestamp(func):
    """Decorator that prints the current time before running the function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(time.ctime())          # e.g. "Wed Oct 19 17:27:12 2022"
        return func(*args, **kwargs) 
    return wrapper
