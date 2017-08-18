from math import sqrt
from pprint import pprint as pp


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        return True


list_compr = [x for x in range(101) if is_prime(x)]
print(list_compr)

dict_compr = {x*x:(1, x, x*x) for x in range(101)
              if is_prime(x)}  # numbers with only three divisors mapped to those divisors
pp(dict_compr)