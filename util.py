from time import time


def timed(func):
    def wrap(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('runtime', time() - start)
        return result

    return wrap
