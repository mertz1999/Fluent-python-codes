# Cach decorator

import functools
import time

# @functools.cache
def fibonacci(n):
    # print("Fibo {} is requested".format(n))
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


last_time = time.time()
print(fibonacci(100))
print(time.time() - last_time)