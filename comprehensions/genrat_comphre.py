from primes import is_prime

gen_comp = (x for x in range(10) if is_prime(x))

if __name__ == '__main__':
    print(list(gen_comp))