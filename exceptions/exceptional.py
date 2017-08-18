''' A module for demonstrating exceptions '''


def convert(s):
    ''' convert to an integer. '''
    x = int(s)
    return x


# if string is passed which is not convertable will throw ValueError exception.