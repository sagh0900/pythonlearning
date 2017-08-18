''' A module for demonstrating exceptions '''


def convert(s):
    ''' convert to an integer. '''
    try:
        x = int(s)
        print("conversion succeeded! x =", x)
    except (ValueError, TypeError):
        #  print("conversion failed!")
        pass
    return x


# if string is passed which is not convertable will throw ValueError exception.