# A decorator that logs function calls
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b

# Call the decorated function
result = add_numbers(2, 3)