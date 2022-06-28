import itertools
import time
from threading import Thread, Event
import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True

def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow() -> int:
    # time.sleep(3)
    is_prime(5_000_111_000_222_021)
    return "Sleep completed"

def supervisor() -> int: 
    done = Event() 
    spinner = Thread(target=spin, args=('thinking!', done))  
    print(f'spinner object: {spinner}')  
    spinner.start() 
    result = slow() 
    done.set()
    spinner.join()
    return result
   
    

if __name__ == '__main__':
    result = supervisor()
    print(f'Answer: {result}')