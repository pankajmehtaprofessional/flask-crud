def custom_middleware(func):
    def wrapper(*args, **kwargs):
        print("-- Before Request --", args, kwargs)
        result = func(*args, **kwargs)
        print("-- After Request --")

        return result
    return wrapper
    