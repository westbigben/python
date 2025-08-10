# Example of a simple decorator

def log_function_call(func):
    """Decorator that logs when a function is called."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result
    return wrapper

@log_function_call
def greet(name):
    print(f"Hello, {name}!")

greet("Pythonista")