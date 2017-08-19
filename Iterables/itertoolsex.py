from itertools import islice, count
from math import sqrt

# islice performs the lazy slicing


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        return True

thousand_primes = islice((x for x in count() if is_prime(x)), 10)

if __name__ == '__main__':
    print("".join(str(list(thousand_primes))))
    print("".join(str(sum(islice((x for x in count() if is_prime(x)), 10)))))
    print(''.join(str(any(is_prime(x) for x in range(13, 17)))))
