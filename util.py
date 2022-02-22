from time import time


def timed(func):
    def wrap(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('runtime', time() - start)
        return result

    return wrap


def is_ge(val, name, minimum):
    assert val >= minimum, f'Too few {name}. Found {val}, should be at least {minimum}.'
