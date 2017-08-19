#  prints values till computer runs out of memory, forced termination needed.
from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        return True


def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a+ b

if __name__ == '__main__':
    obj = []
    for x in (p for p in lucas() if is_prime(p)):
        obj.append(x)

    print(obj)