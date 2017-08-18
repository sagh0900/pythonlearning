''' A module for demonstrating exceptions '''
import sys
from math import log


def convert(s):
    """converting integer literal in string representation to int
     convert to an integer."""
    try:
        x = int(s)
        print("conversion succeeded! x =", x)
        return x
    except (ValueError, TypeError) as e:
        print("conversion error: {}"
              .format(str(e)),
              file=sys.stderr)
        raise


def string_log(s):
    v = convert(s)
    return log(v)


# if string is passed which is not convertable will throw ValueError exception.