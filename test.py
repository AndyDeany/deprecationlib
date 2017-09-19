from functools import wraps
import warnings


warnings.simplefilter("always", DeprecationWarning)

def deprecated(alternative):
    if callable(alternative):
        @wraps(alternative)
        def deprecated_function(*args, **kwargs):
            warnings.warn(f"{alternative.__name__}() is deprecated. Please use an alternative instead.", DeprecationWarning)
            return alternative(*args, **kwargs)
        return deprecated_function
    def decorator(function):
        @wraps(function)
        def deprecated_function(*args, **kwargs):
            warnings.warn(f"{function.__name__}() is deprecated. Please use {alternative} instead.", DeprecationWarning)
            return function(*args, **kwargs)
        return deprecated_function
    return decorator


@deprecated("hi")
def yes(a, b):
    print(a, b)

@deprecated
def no(a, b):
    print(a, b)

