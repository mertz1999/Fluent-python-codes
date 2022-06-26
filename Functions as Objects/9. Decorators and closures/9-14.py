import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        print(f'time: {elapsed}')
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


print("Snooze")
snooze(.123)

print("\nFactorial")
factorial(6)

# if __name__ == '__main__':
#     print('*' * 40, 'Calling snooze(.123)')
#     snooze(.123)
#     print('*' * 40, 'Calling factorial(6)')
#     print('6! =', factorial(6))