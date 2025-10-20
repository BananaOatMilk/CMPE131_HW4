from functools import wraps

def allcaps(func):
    """Decorator: if the wrapped function returns a string, return it uppercased."""
    @wraps(func)
    def wrapper():
        result = func()                 
        return result.upper() if isinstance(result, str) else result
    return wrapper
