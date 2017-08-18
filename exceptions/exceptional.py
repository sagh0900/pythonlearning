''' A module for demonstrating exceptions '''


def convert(s):
    ''' convert to an integer. '''
    try:
        x = int(s)
        print("conversion succeeded! x =", x)
    except ValueError:
        print("conevsrion failed")
        x = -1
    except TypeError:
        print("cannot convert collection object, x =", s)
    return x


# if string is passed which is not convertable will throw ValueError exception.