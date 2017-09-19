from functools import wraps
import warnings


warnings.simplefilter("always", DeprecationWarning)

def deprecated(alternative_or_function):
    def warn(func, alt):
        message = f"{func.__name__}() is deprecated. Please use {alt} instead."
        warnings.warn(message, DeprecationWarning)

    if callable(alternative_or_function):
        @wraps(alternative_or_function)
        def deprecated_function(*args, **kwargs):
            warn(alternative_or_function, "an alternative")
            return alternative_or_function(*args, **kwargs)
        return deprecated_function

    def decorator(function):
        @wraps(function)
        def deprecated_function(*args, **kwargs):
            warn(function, alternative_or_function)
            return function(*args, **kwargs)
        return deprecated_function
    return decorator


@deprecated("hi")
def yes(a, b):
    print(a, b)

@deprecated
def no(a, b):
    print(a, b)

