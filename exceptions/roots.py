import sys

def sqrt(x):
    """ Compute square roots using method of heron of Alexandria.
    
    Args:
        x:  The number for which square root is to be computed
        
    Returns:
        The square root of x
    """
    if x < 0:
        raise ValueError("Cannot compute a square root of a negative number {}"
                         .format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))  # will raise ZeroDivisionError exception
        print("This never printed")
    except ValueError as e:
        print(e, file=sys.stderr)

    print("Program Execution continues normally")


if __name__ == '__main__':
    main()



